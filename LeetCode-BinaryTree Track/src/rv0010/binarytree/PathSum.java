package rv0010.binarytree;

class PathSum {
    private int s;

    public boolean hasPathSum(TreeNode root, int sum) {
        s = sum;
        return equalSum(root, 0);
    }

    private boolean equalSum(TreeNode node, int currSum) {
        if (node == null) {
            return false;
        }
        currSum += node.val;
        if (node.left == null && node.right == null && currSum == s) {
            return true;
        } else {
            return (equalSum(node.left, currSum) || equalSum(node.right, currSum));
        }
    }
}
