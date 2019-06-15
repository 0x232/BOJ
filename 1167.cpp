#include <cstdio>
#include <vector>
#include <stack>
#include <algorithm>

using namespace std;

vector<pair<int, int>> edge[100001];
bool visited[100001] = { false };

int main() {
	int V;
	scanf("%d", &V);

	for (int i = 0; i < V; i++) {
		int v1;
		scanf("%d", &v1);
		int v2, d;
		scanf("%d", &v2);
		while (v2 != -1) {
			scanf("%d", &d);
			edge[v1].push_back(make_pair(v2, d));
			scanf("%d", &v2);
		}
	}

	stack<int> s;
	vector<int> d(V + 1);
	s.push(1);
	d[1] = 0;
	while (!s.empty()) {
		int v = s.top();
		visited[v] = true;
		s.pop();
		for (int i = 0; i < edge[v].size(); i++) {
			if (!visited[edge[v][i].first]) {
				s.push(edge[v][i].first);
				d[edge[v][i].first] = d[v] + edge[v][i].second;
			}
		}
	}

	int f = distance(d.begin(), max_element(d.begin(), d.end()));
	for (int i = 1; i <= V; i++) {
		visited[i] = false;
	}
	for (int i = 1; i <= V; i++) {
		d[i] = 0;
	}
	s.push(f);
	d[f] = 0;
	while (!s.empty()) {
		int v = s.top();
		visited[v] = true;
		s.pop();
		for (int i = 0; i < edge[v].size(); i++) {
			if (!visited[edge[v][i].first]) {
				s.push(edge[v][i].first);
				d[edge[v][i].first] = d[v] + edge[v][i].second;
			}
		}
	}

	printf("%d", *max_element(d.begin(), d.end()));

	return 0;
}