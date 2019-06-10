#include <cstdio>
#include <vector>
#include <queue>

using namespace std;

int parent[100001] = { 0 };
vector<int> edge[100001];

int main() {
	int N;
	scanf("%d", &N);
	for (int i = 0; i < N - 1; i++) {
		int v1, v2;
		scanf("%d %d", &v1, &v2);
		edge[v1].push_back(v2);
		edge[v2].push_back(v1);
	}
	
	queue<int> visited;
	visited.push(1);
	while (!visited.empty()) {
		int root = visited.front();
		visited.pop();
		for (int i = 0; i < edge[root].size(); i++) {
			if (parent[edge[root][i]] == 0) {
				parent[edge[root][i]] = root;
				visited.push(edge[root][i]);
			}
		}
	}

	for (int i = 2; i <= N; i++) {
		printf("%d\n", parent[i]);
	}

	return 0;
}