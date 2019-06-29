#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> numbers;
vector<int> op;
int add = 0, subtract = 1, multiply = 2, divide = 3;
vector<bool> visited;
int minValue = -1e9, maxValue = 1e9;

void calculate(vector<int>& picked) {
	int result = numbers[0];
	for (size_t i = 0; i < picked.size(); i++) {
		if (picked[i] == add)
			result += numbers[i + 1];
		if (picked[i] == subtract)
			result -= numbers[i + 1];
		if (picked[i] == multiply)
			result *= numbers[i + 1];
		if (picked[i] == divide)
			result /= numbers[i + 1];
	}
	if (minValue == -1e9)
		minValue = result;
	if (maxValue == 1e9)
		maxValue = result;
	minValue = min(result, minValue);
	maxValue = max(result, maxValue);
}

void pick(int N, int toPick, vector<int>& picked) {
	if (toPick == 0) {
		calculate(picked);
		return;
	}
	for (int i = 0; i < N; i++) {
		if (!visited[i]) {
			visited[i] = true;
			picked.push_back(op[i]);
			pick(N, toPick - 1, picked);
			visited[i] = false;
			picked.pop_back();
		}
	}
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	int N;
	cin >> N;
	numbers.resize(N);
	for (int i = 0; i < N; i++)
		cin >> numbers[i];
	int numberOfOperator[4];
	for (int i = 0; i < 4; i++)
		cin >> numberOfOperator[i];
	op.resize(N - 1);
	vector<int>::iterator iter = op.begin();
	for (int i = 0; i < 4; i++) {
		fill(iter, iter + numberOfOperator[i], i);
		iter += numberOfOperator[i];
	}
	visited.resize(N - 1, false);
	vector<int> picked;
	pick(N - 1, N - 1, picked);
	cout << maxValue << '\n' << minValue;
	return 0;
}