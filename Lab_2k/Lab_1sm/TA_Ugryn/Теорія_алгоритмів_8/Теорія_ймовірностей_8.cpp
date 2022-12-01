#include <bits/stdc++.h>
#include <iostream>

using namespace std;
class Node
{
public:
	int data;
	Node* left, * right;
	/* Конструктор, який виділяє новий
вузол із заданими даними та NULL
лівий і правий показники. */
	Node(int data)
	{
		this->data = data;
		this->left = NULL;
		this->right = NULL;
	}
};
// Повернути максимум
// Саме бінарне дерево
int findMax(Node* root)
{
	// знайти максимальне
	if (root == NULL)
		return INT_MIN;
	int res = root->data;
	int lres = findMax(root->left);
	int rres = findMax(root->right);
	if (lres > res)
		res = lres;
	if (rres > res)
		res = rres;
	return res;
}
int findMin(Node* root)
{
	//знайти мінімальне
	if (root == NULL)
	{
		return INT_MAX;
	}
	int res = root->data;
	int left = findMin(root->left);
	int right = findMin(root->right);
	if (left < res)
	{
		res = left;
	}
	if (right < res)
	{
		res = right;
	}
	return res;
}
int countOccurrences(Node* root)
{
	int res = 0;
	if (root == data)
		res++;
	return res;
}
int addBT(Node* root)
{
	if (root == NULL)
		return 0;
	return (root->data + addBT(root->left) + addBT(root->right));
}
int inOrder(Node* root)
{
	if (root != NULL)
	{
		inOrder(root->left);
		cout << root->data << " ";
		inOrder(root->right);
	}
}
// Код виклику
int main()
{
	setlocale(LC_ALL, "Ukr");

	Node* NewRoot = NULL;
	Node* root = new Node(2);
	root->left = new Node(7);
	root->right = new Node(5);
	root->left->right = new Node(6);
	root->left->left = new Node(4);
	root->left->right->left = new Node(1);
	root->left->right->right = new Node(11);
	root->right->right = new Node(9);
	root->right->right->left = new Node(4);
	// Виклик функції
	cout << "- - - - - - - - - - - - - - - " << endl;
	cout << "Всі елементи: " << inOrder(root) << endl;
	cout << "- - - - - - - - - - - - - - -" << endl;
	cout << "Максимальний елемент: " << findMax(root) << endl;
	cout << "Мінімальний елемент: " << findMin(root) << endl;
	cout << "Дерево кількох елементів: " << countOccurrences(root) << endl;
	cout << "Сума всіх елементів дерева: " << addBT(root) << endl;
	return 0;
}
