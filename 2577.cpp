#include <iostream>

using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	int A, B, C;
	cin >> A >> B >> C;
	int result = A * B * C;
	int digit[10] = { 0 };
	while (result > 0) {
		digit[result % 10]++;
		result /= 10;
	}
	for (auto x : digit) {
		cout << x << '\n';
	}

	return 0;
}