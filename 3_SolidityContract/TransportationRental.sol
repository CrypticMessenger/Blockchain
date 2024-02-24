// SPDX-License-Identifier: MIT
pragma solidity >=0.6.12 <0.9.0;

contract TransportationRental {
    // GLOBAL VARS
    address payable public owner; // Address of the contract owner
    uint256 public depositAmount; // Deposit amount required to rent a cycle
    uint256 public cycleCount; // Total number of cycles available
    uint256 public remCycleCount; // Number of cycles currently available
    bool public paused; // Whether the contract is paused

    // MAPS
    mapping(address => Ride[]) public rides; // Mapping of user addresses to their rides
    mapping(uint256 => address) public cycleIdToUser; // Mapping of cycle IDs to the user currently renting them

    // STRUCTS
    struct Ride {
        uint256 startTime; // Timestamp of the ride start
        uint256 endTime; // Timestamp of the ride end (0 if ongoing)
        uint256 distance; // Distance travelled (randomly generated)
        uint256 speed; // Average speed calculated after ride ends
        uint256 deposit; // Deposit amount paid by the user
        bool completed; // Whether the ride is completed
        uint256 cycleId; // ID of the cycle used for the ride
    }

    // EVENTS
    event RideStarted(address indexed user, uint256 rideId); // Event emitted when a ride starts
    event RideEnded(address indexed user, uint256 rideId);  // Event emitted when a ride ends

    // Constructor initializes contract state
    constructor(uint256 _depositAmount, uint256 _cycleCount) {
        owner = payable(msg.sender);
        depositAmount = _depositAmount;
        cycleCount = _cycleCount;
        remCycleCount = cycleCount;
        paused = false;

        // Initialize cycleIdToUser mapping with empty addresses
        for (uint256 i = 0; i < cycleCount; i++) {
            cycleIdToUser[i] = address(0);
        }
    }

    // CUSTOM MODIFIERS
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }
    modifier notPaused() {
        require(!paused, "Rentals are currently paused");
        _;
    }

    // Start a new ride
    function startRide() external payable notPaused{
        require(remCycleCount > 0, "No cycles available"); // Check if cycles are available
        require(depositAmount <= msg.sender.balance, "Insufficient balance in the account"); // Check if user has sufficient balance
        require(msg.value >= depositAmount, "Trying to send insufficient deposit amount"); // Check if deposit amount is correct

        // Ensure user doesn't have an uncompleted ride
        uint256 len = rides[msg.sender].length;
        if (len != 0) {
            Ride storage ride = rides[msg.sender][len - 1];
            require(!ride.completed, "You already have an uncompleted ride");
        }
        
        remCycleCount--; // Decrement available cycles
        
        uint256 cycleId = 0; // Find an available cycle
        for (uint256 i = 0; i < cycleCount; i++) {
            if (cycleIdToUser[i] == address(0)) {
                cycleId = i;
                cycleIdToUser[i] = msg.sender;
                break;
            }
        }
        
        Ride memory newRide = Ride(block.timestamp, 0, 0, 0, msg.value, false, cycleId); // Create a new ride record
        rides[msg.sender].push(newRide);
        
        owner.transfer(msg.value); // Transfer deposit to owner
        emit RideStarted(msg.sender, cycleId); // Emit RideStarted event
    }

    // End an ongoing ride
    function endRide() external {
        uint256 len = rides[msg.sender].length;
        require(len != 0, "No ride to end!"); // Check if user has rides
        
        Ride storage ride = rides[msg.sender][len - 1]; // Get the last ride
        require(!ride.completed, "No ride to end!");  // Ensure the ride is ongoing

        ride.endTime = block.timestamp; // Set the end time of the ride
        cycleIdToUser[ride.cycleId] = address(0); // Free up the cycle

        remCycleCount++; // Increment available cycles
        // Generate a random distance between 0 and 40 km (40000 meters)
        ride.distance = uint256(keccak256(abi.encodePacked(block.timestamp, msg.sender))) % 40000;
        ride.speed = (ride.distance) / (ride.endTime - ride.startTime); //average speed in m/s

        ride.completed = true; // Mark the ride as completed

        emit RideEnded(msg.sender, ride.cycleId); // Emit RideEnded event
    }

    function changeDepositAmount(uint256 newDepositAmount) public onlyOwner {
        depositAmount = newDepositAmount;
    }
    function addCycles(uint256 additionalCycles) public onlyOwner {
        cycleCount += additionalCycles;
        remCycleCount += additionalCycles;

        // Update cycleIdToUser mapping with empty addresses for the new cycles
        for (uint256 i = cycleCount - additionalCycles; i < cycleCount; i++) {
            cycleIdToUser[i] = address(0);
        }
    }
    function pauseRentals() public onlyOwner {
        paused = true;
    }

    function unpauseRentals() public onlyOwner {
        paused = false;
    }
}