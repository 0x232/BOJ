#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

void printPicked(vector<int>& picked) {
	for (int i = 0; i < picked.size(); i++)
		cout << picked[i] << ' ';
	cout << '\n';
}

void pick(int N, int M, vector<bool>& visited, vector<int>& numbers, vector<int>& picked) {
	if (M == 0) {
		printPicked(picked);
		return;
	}
	for (int i = 0; i < N; i++) {
		if (!visited[i]) {
			visited[i] = true;
			picked.push_back(numbers[i]);
			pick(N, M - 1, visited, numbers, picked);
			visited[i] = false;
			picked.pop_back();
		}
	}
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	int N, M;
	cin >> N >> M;
	vector<bool> visited(N, false);
	vector<int> numbers;
	for (int i = 0; i < N; i++) {
		int number;
		cin >> number;
		numbers.push_back(number);
	}
	sort(numbers.begin(), numbers.end());
	vector<int> picked;
	pick(N, M, visited, numbers, picked);
	return 0;
}