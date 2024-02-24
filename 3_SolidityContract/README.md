# Assumptions

- The Amount gets deducted when the user starts the ride.
- The pricing is constant and does not change with time.
- The distance travelled is in meters and assigned randomly. (simulating the real world scenario)
- User can rent only one vehicle at a time.
- All the amounts are by default in wei. (in remix IDE)

# Owner capabilities

- Owner can add new vehicles to the system. (`addCycles(uint256 additionalCycles)`)
- Owner can change the price of the ride. (`changeDepositAmount(uint256 _newAmount)`)
- Owner can pause rental system anytime he/she wants. (`pauseRental(), unpauseRentals()`)
- Coded custom modifiers to check if the owner is calling the function.

# User capabilities

- User can rent a vehicle only if the rental services are un-paused. (`startRide()`)
- User can end the ride. (`endRide()`)

# Testing

- Testing is done by deploying on sepolia testnet and using the remix IDE.
- contract is deployed on the sepolia testnet and the contract address is `0xf4CC43B586Ee88ECf09f70236B98A0Af72e51b8B`
- visit to see history of contract: https://sepolia.etherscan.io/address/0xf4CC43B586Ee88ECf09f70236B98A0Af72e51b8B
