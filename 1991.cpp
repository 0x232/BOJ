#include <iostream>

using namespace std;

struct Node {
	char data;
	struct Node *left = nullptr, *right = nullptr;
};

void preorder(Node *root) {
	if (!root) {
		return;
	}
	cout << root->data;
	preorder(root->left);
	preorder(root->right);
}

void inorder(Node *root) {
	if (!root) {
		return;
	}
	inorder(root->left);
	cout << root->data;
	inorder(root->right);
}

void postorder(Node *root) {
	if (!root) {
		return;
	}
	postorder(root->left);
	postorder(root->right);
	cout << root->data;
}

int main() {
	Node tree[26];
	for (int i = 0; i < 26; i++) {
		tree[i].data = char(i + 65);
	}

	int N;
	cin >> N;
	for (int i = 0; i < N; i++) {
		char root, left, right;
		cin >> root >> left >> right;
		if (left != '.') {
			tree[int(root - 65)].left = &(tree[int(left - 65)]);
		}
		if (right != '.') {
			tree[int(root - 65)].right = &(tree[int(right - 65)]);
		}
	}

	Node *root = &(tree[0]);
	preorder(root);
	cout << '\n';
	inorder(root);
	cout << '\n';
	postorder(root);
	cout << '\n';

	return 0;
}