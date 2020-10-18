// C++ implementation of the approach 
#include <bits/stdc++.h> 
using namespace std; 

#define size 2 

// Function to perform the required 
// queries on the given string 
void performQueries(string str, int n, 
					int queries[][size], int q) 
{ 

	// Pointer pointing to the current starting 
	// character of the string 
	int ptr = 0; 

	// For every query 
	for (int i = 0; i < q; i++) { 

		// If the query is to rotate the string 
		if (queries[i][0] == 1) { 

			// Update the pointer pointing to the 
			// starting character of the string 
			ptr = (ptr + queries[i][1]) % n; 
		} 
		else { 

			int k = queries[i][1]; 

			// Index of the kth character in the 
			// current rotation of the string 
			int index = (ptr + k - 1) % n; 

			// Print the kth character 
			cout << str[index] << "\n"; 
		} 
	} 
} 

// Driver code 
int main() 
{ 
	string str = "abcdefgh"; 
	int n = str.length(); 

	int queries[][size] = { { 1, 2 }, { 2, 2 }, 
							{ 1, 4 }, { 2, 7 } }; 
	int q = sizeof(queries) / sizeof(queries[0]); 

	performQueries(str, n, queries, q); 

	return 0; 
} 
