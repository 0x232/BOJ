#include <iostream>
#include <algorithm>

using namespace std;

bool isBroken[10];

/*
10
9
1 2 3 4 5 6 7 8 9
답:11
*/

int numberOfPush(int N) {
	int channel = N;
	int closestChannel = 0;
	int pow = 1;
	int numberOfPush = 0;
	while (N > 0) {
		int distance = 10, closest = -1;
		for (int i = 0; i < 10; i++) {
			if (!isBroken[i]) {
				if (distance > abs(N % 10 - i)) {
					distance = abs(N % 10 - i);
					closest = i;
				}
			}
		}
		N /= 10;
		closestChannel += closest * pow;
		pow *= 10;
		numberOfPush++;
	}
	return min(abs(channel - 100), abs(channel - closestChannel) + numberOfPush);
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	int N;
	cin >> N;
	int numberOfBrokenButton;
	cin >> numberOfBrokenButton;
	for (int i = 0; i < numberOfBrokenButton; i++) {
		int button;
		cin >> button;
		isBroken[button] = true;
	}
	cout << numberOfPush(N);
	return 0;
}