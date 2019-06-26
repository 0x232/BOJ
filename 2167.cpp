#include <iostream>

using namespace std;

int arr[300][300];

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	int N, M;
	cin >> N >> M;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			cin >> arr[i][j];
		}
	}
	int K;
	cin >> K;
	for (int k = 0; k < K; k++) {
		int i, j, x, y;
		cin >> i >> j >> x >> y;
		int sum = 0;
		for (int n = i - 1; n <= x - 1; n++) {
			for (int m = j - 1; m <= y - 1; m++) {
				sum += arr[n][m];
			}
		}
		cout << sum << '\n';
	}
}