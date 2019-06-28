#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

void printPicked(vector<int>& picked) {
	for (int i = 0; i < picked.size(); i++)
		cout << picked[i] << ' ';
	cout << '\n';
}

void pick(int N, int M, vector<int>& numbers, vector<int>& picked, int smallest_index) {
	if (M == 0) {
		printPicked(picked);
		return;
	}
	for (int i = smallest_index; i < N; i++) {
		picked.push_back(numbers[i]);
		pick(N, M - 1, numbers, picked, i+1);
		picked.pop_back();
	}
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	int N, M;
	cin >> N >> M;
	vector<int> numbers;
	for (int i = 0; i < N; i++) {
		int number;
		cin >> number;
		numbers.push_back(number);
	}
	sort(numbers.begin(), numbers.end());
	vector<int> picked;
	pick(N, M, numbers, picked, 0);
	return 0;
}