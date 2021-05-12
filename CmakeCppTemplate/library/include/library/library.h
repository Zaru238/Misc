#pragma once

#include <vector>

struct TreeNode {
  int val;
  TreeNode *left;
  TreeNode *right;
  TreeNode() : val(0), left(nullptr), right(nullptr) {}
  TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
  TreeNode(int x, TreeNode *left, TreeNode *right)
      : val(x), left(left), right(right) {}
};

class Solution {
 public:
  auto findTilt(TreeNode *root) -> int;

 private:
  std::vector<int> tilt_sum_table_;

  auto findTiltHelper(TreeNode *node) -> int;
};

void foo();
