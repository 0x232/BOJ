#include <iostream>
#include <vector>

using namespace std;

void printPicked(vector<int>& picked) {
	for (int i = 0; i < picked.size(); i++)
		cout << picked[i] << ' ';
	cout << '\n';
}

void pick(int N, int M, vector<int>& picked) {
	if (M == 0) {
		printPicked(picked);
		return;
	}
	for (int i = 0; i < N; i++) {
		picked.push_back(i + 1);
		pick(N, M - 1, picked);
		picked.pop_back();
	}
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	int N, M;
	cin >> N >> M;
	vector<int> picked;
	pick(N, M, picked);
	return 0;
}