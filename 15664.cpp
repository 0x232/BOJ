#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<bool> visited;
vector<int> numbers;
vector<vector<int>> permutations;

void printPicked(vector<int>& picked) {
	for (int i = 0; i < picked.size(); i++)
		cout << picked[i] << ' ';
	cout << '\n';
}

void pick(int N, int M, vector<int>& picked, int smallest_index) {
	if (M == 0) {
		permutations.push_back(picked);
		return;
	}
	for (int i = smallest_index; i < N; i++) {
		picked.push_back(numbers[i]);
		pick(N, M - 1, picked, i + 1);
		picked.pop_back();
	}
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	int N, M;
	cin >> N >> M;
	// Initialization.
	visited.resize(N, false);
	numbers.resize(N);
	for (int i = 0; i < N; i++)
		cin >> numbers[i];
	sort(numbers.begin(), numbers.end());
	vector<int> picked;
	pick(N, M, picked, 0);
	// Remove duplicates.
	sort(permutations.begin(), permutations.end());
	permutations.erase(unique(permutations.begin(), permutations.end()), permutations.end());
	// Print permutations.
	for (int i = 0; i < permutations.size(); i++)
		printPicked(permutations[i]);
	return 0;
}