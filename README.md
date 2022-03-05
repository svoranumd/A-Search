# A*Search
## Windy 8-Puzzle Problem
<img width="100" alt="image" src="https://user-images.githubusercontent.com/79284398/156876124-b0f3f916-c792-4e65-a8ee-da3d3a2729ee.png"> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; <img width="100" alt="image" src="https://user-images.githubusercontent.com/79284398/156876186-480ddd03-c92f-4727-a878-c103da629d32.png"><br>
### Movement Cost With South Wind
- 1 Northward 
- 2 Westward or Eastward
- 3 Southward </ul>
### Implementation
- A priotiry queue is used for the frontier set, and a hash table <br>
for the explored set. <br>
- When expanding the current node, our code follows the order of swapping <br>
the "0" tile first westward, then northward, then eastward, then southward.<br>
- We use FIFO when mutiple nodes have the same total cost</ul>
### Key
- The puzzle is printed in a block, 3 x 3 format
- The number on the bottom left is the path cost
- The number on the bottom right is the total Manhattan distance
- The bottom number is the current expansion number </ul>
### Results
<img width="71" alt="image" src="https://user-images.githubusercontent.com/79284398/156877149-531aefb3-7d25-4839-8a59-7d603a175e4a.png">&nbsp; &nbsp;<img width="64" alt="image" src="https://user-images.githubusercontent.com/79284398/156877175-27c124c3-3740-466e-8442-c29125cb5df8.png">&nbsp; &nbsp;<img width="62" alt="image" src="https://user-images.githubusercontent.com/79284398/156877205-ef3826fc-c550-4c50-bff9-d32c1f8daa92.png">&nbsp; &nbsp;<img width="62" alt="image" src="https://user-images.githubusercontent.com/79284398/156877228-9114a9a6-3285-4e61-be28-e9fa767974a5.png">&nbsp; &nbsp;<img width="69" alt="image" src="https://user-images.githubusercontent.com/79284398/156877239-360bcbf0-8d96-409e-ae39-18a47e8bdcdd.png">
<br>**Editor: Skyler Voran <br>
Creation Date: 02/14/2022** <br>
