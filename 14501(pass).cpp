#include <iostream>

using namespace std;

int N, T[15], P[15], maxProfit = 0;
bool visited[15];

void pick(int time, int profit) {
	// Base Condition
	if (time > N)
		return;
	if (time == N) {
		maxProfit = profit > maxProfit ? profit : maxProfit;
		return;
	}
	//
	if (time+T[time]<N)
		pick(time + T[time], profit + P[time]);
	pick(time + 1, profit);
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	
	cin >> N;
	for (int i = 0; i < N; i++)
		cin >> T[i] >> P[i];
	
	pick(0, 0);
	cout << maxProfit;

	return 0;
}