#include <iostream>
#include <string>

using namespace std;

int main() {
	string s;
	cin >> s;

	int a[26] = { 0 };
	for (auto c : s)
		a[c - 97]++;

	for (auto x: a)
		cout << x << ' ';

	return 0;
}