#include <iostream>
#include <algorithm>

using namespace std;

int numbers[11];
int minValue = 1e9, maxValue = -1e9;

void pick(int N, int toPick, int a, int s, int m, int d, int result) {
	if (toPick == 0) {
		minValue = min(result, minValue);
		maxValue = max(result, maxValue);
		return;
	}
	if (a > 0)
		pick(N, toPick - 1, a - 1, s, m, d, result + numbers[N - toPick]);
	if (s > 0)
		pick(N, toPick - 1, a, s - 1, m, d, result - numbers[N - toPick]);
	if (m > 0)
		pick(N, toPick - 1, a, s, m - 1, d, result * numbers[N - toPick]);
	if (d > 0)
		pick(N, toPick - 1, a, s, m, d - 1, result / numbers[N - toPick]);
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	int N;
	cin >> N;
	for (int i = 0; i < N; i++)
		cin >> numbers[i];
	int a, s, m, d;
	cin >> a >> s >> m >> d;
	pick(N, N-1, a, s, m, d, numbers[0]);
	cout << maxValue << '\n' << minValue;
	return 0;
}