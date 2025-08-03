# Signal exchange between Python and FactoryIO via Modbus.

## Digital Input
| Input Number | Tag | Description |
|--------------|-----|-------------|
| Input 0 | FACTORY I/O (Running) | Status if FactoryIO is running, this is used to reset out program, if its False |
| Input 1 | Group Start | Button on Control Cabinet to Start Group (0 = False, 1 = True) |
| Input 2 | Group Stop | Button on Control Cabinet to Stop Group (0 = True, 0 = False) |
| Input 3 | Unused Input | Available
| Input 4 | Unused Input | Available
| Input 5 | Unused Input | Available
| Input 6 | Unused Input | Available
| Input 7 | Unused Input | Available
| Input 8 | Unused Input | Available
| Input 9 | Unused Input | Available
| Input 10 | Input Conveyor 1 B1 | Sensor on Input Conveyor 1, before scale (Stops conveyor is product is on scale)
| Input 11 | Scale Conveyor 1 B1 | Sensor on Scale Conveyor 1, used to register scale of product on scale.
| Input 12 | Output Conveyor 1 B1 | Sensor on Output Conveyor 1, used to place product in sorting register.
| Input 13 | Unused Input | Avaliable
| Input 14 | Unused Input | Available
| Input 15 | Unused Input | Available
| Input 16 | Unused Input | Available
| Input 17 | Unused Input | Available
| Input 18 | Unusud Input | Available
| Input 19 | Unused Input | Available
| Input 20 | Output Conveyor Encoder A | Encoder used to move sorting register forward.
| Input 21 | Unused Input | Available
| Input 22 | Unused Input | Available
| Input 23 | Unused Input | Available
| Input 24 | Unused Input | Available
| Input 25 | Unused Input | Available
| Input 26 | Unused Input | Available
| Input 27 | Unused Input | Available
| Input 28 | Unused Input | Available
| Input 29 | Unused Input | Available
| Input 30 | Unused Input | Available
| Input 31 | Unused Input | Available

## Digital Output
| Output Number | Tag | Description |
|---------------|-----|-------------|
| Output 0 | Group Stopped | Tower Lamp Red, Group is stopped
| Output 1 | Group Starting | Tower Lamp Yellow, Group is starting
| Output 2 | Group Running | Tower Lamp Green, Group is running
| Output 3 | Start Lamp | Button "Group Start" Lamp
| Output 4 | Stop Lamp | Button "Group Stop" Lamp
| Output 5 | Unused Output | Available
| Output 6 | Unused Output | Available
| Output 7 | Unused Output | Available
| Output 8 | Unused Output | Available
| Output 9 | Unused Output | Available
| Output 10 | Sweeper 1 Arm | Control the Arm for Sweeper 1 (Small Package)
| Output 11 | Sweeper 2 Arm | Control the Arm for Sweeper 2 (Medium Package)
| Output 12 | Sweeper 3 Arm | Control the Arm for Sweeper 3 (Large Package)
| Output 13 | Unused Output | Available
| Output 14 | Unused Output | Available
| Output 15 | Product Spawn | Enable products to be spawned on Input Conveyor
| Output 16 | Unused Output | Available
| Output 17 | Unused Output | Available
| Output 18 | Unused Output | Available
| Output 19 | Unused Output | Available
| Output 20 | Input Conveyor 1 (F) | Starts Input Conveyor 1 in Forward Direction
| Output 21 | Scale Conveyor 1 (F) | Starts Scale Conveyor 1 in Forward Direction
| Output 22 | Output Conveyor 1 (F) | Starts Output Conveyor 1 in Forward Direction
| Output 23 | Output Conveyor 2 (F) | Starts Output Conveyor 2 in Forward Direction
| Output 24 | Small Box Conveyor 1 (F) | Starts Small Box Conveyor 1 in Forward Direction
| Output 25 | Medium Box Conveyor 1 (F) | Starts Medium Box Conveyor 1 in Forward Direction
| Output 26 | Large Box Conveyor 1 (F) | Starts Large Box Conveyor 1 in Forward Direction
| Output 27 | Sweeper 1 Motor (F) | Starts Sweeper 1 Motor in Forward Direction
| Output 28 | Sweeper 2 Motor (F) | Starts Sweeper 2 Motor in Forward Direction
| Output 29 | Sweeper 3 Motor (F) | Starts Sweeper 3 Motor in Forward Direction
| Output 30 | Unused Output | Available
| Output 31 | Unused Output | Available

## Analog Input
| Register Number | Tag | Description |
|-----------------|-----|-------------|
| Register 0 | Scale 1 (0-20Kg) | Returns value from Scale, Value 1000 = 10Kg.