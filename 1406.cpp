#include <iostream>
#include <string>
#include <list>

using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	string s;
	cin >> s;

	list<char> l;
	for (auto c : s)
		l.push_back(c);

	int N;
	cin >> N;

	auto cursor = l.end();
	getline(cin, s);
	for (int i = 0; i < N; i++) {
		string command;
		getline(cin, command);
		if (command[0] == 'L') {
			if (cursor != l.begin())
				cursor--;
		}
		if (command[0] == 'D') {
			if (cursor != l.end())
				cursor++;
		}
		if (command[0] == 'B') {
			if (cursor != l.begin())
				cursor = l.erase(--cursor);
		}
		if (command[0] == 'P') {
			l.insert(cursor, command[2]);
		}
	}

	for (auto x : l) {
		cout << x;
	}

	return 0;
}