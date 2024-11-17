#sorting 

%%
[[Git Ignore/Heavy Stuff/Uni PDFs/algorithmics rotated cropped.pdf#page=64|algorithmics rotated cropped, p.64]]
[[Git Ignore/Heavy Stuff/Matthew Barnes Notes/Algorithmics Notes.pdf#page=61|Algorithmics Notes, p.61]]
%%

![[Images/algorithmics rotated cropped 6.png|400]]

%%[[Git Ignore/Heavy Stuff/Uni PDFs/algorithmics rotated cropped.pdf#page=64&rect=66,356,419,545|algorithmics rotated cropped, p.64]]%%

- Splits the list into subgroups, then regroups them
- Once all elements are split into singleton groups, they are each compared and appended to each other

%%[[Git Ignore/Heavy Stuff/Matthew Barnes Notes/Algorithmics Notes.pdf#page=61&selection=6,0,12,22&color=yellow|Algorithmics Notes, p.61]]%%

# Algorithm

```
procedure MergeSort(a, start, end)
    if start < end then
        mid ← (start + end) / 2
        MergeSort(a, start, mid)
        MergeSort(a, mid + 1, end)
        Merge(a, start, mid, end)
    else
        return
```

```java
// Merges two subarrays of arr[].
// First subarray is arr[l..m]
// Second subarray is arr[m+1..r]
static void merge(int arr[], int l, int m, int r) {
	// Find sizes of two subarrays to be merged
	int n1 = m - l + 1;
	int n2 = r - m;

	// Create temp arrays
	int L[] = new int[n1];
	int R[] = new int[n2];

	// Copy data to temp arrays
	for (int i = 0; i < n1; ++i)
		L[i] = arr[l + i];
	for (int j = 0; j < n2; ++j)
		R[j] = arr[m + 1 + j];

	// Merge the temp arrays

	// Initial indices of first and second subarrays
	int i = 0, j = 0;

	// Initial index of merged subarray array
	int k = l;
	while (i < n1 && j < n2) {
		if (L[i] <= R[j]) {
			arr[k] = L[i];
			i++;
		}
		else {
			arr[k] = R[j];
			j++;
		}
		k++;
	}

	// Copy remaining elements of L[] if any
	while (i < n1) {
		arr[k] = L[i];
		i++;
		k++;
	}

	// Copy remaining elements of R[] if any
	while (j < n2) {
		arr[k] = R[j];
		j++;
		k++;
	}
}

// Main function that sorts arr[l..r] using
// merge()
static void sort(int arr[], int l, int r) {
	if (l < r) {

		// Find the middle point
		int m = l + (r - l) / 2;

		// Sort first and second halves
		sort(arr, l, m);
		sort(arr, m + 1, r);

		// Merge the sorted halves
		merge(arr, l, m, r);
	}
}
```

# Example

![[Images/Algorithmics Notes 2.png]]

%%[[Git Ignore/Heavy Stuff/Matthew Barnes Notes/Algorithmics Notes.pdf#page=61&rect=70,104,528,293&color=yellow|Algorithmics Notes, p.61]]%%

![[Images/merge-sort.gif|400]]