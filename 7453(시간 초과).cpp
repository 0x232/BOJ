#include <iostream>

using namespace std;

int N, A[4000], B[4000], C[4000], D[4000], cnt;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cin >> N;
	for (int i = 0; i < N; i++)
		cin >> A[i] >> B[i] >> C[i] >> D[i];
	for (int a = 0; a < N; a++) {
		for (int b = 0; b < N; b++) {
			for (int c = 0; c < N; c++) {
				for (int d = 0; d < N; d++) {
					if (A[a] + B[b] + C[c] + D[d] == 0)
						cnt++;
				}
			}
		}
	}
	cout << cnt;
	return 0;
}