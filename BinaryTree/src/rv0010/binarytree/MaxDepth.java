package rv0010.binarytree;

class MaxDepth {
    private int answer = 0;

    public int maxDepth(TreeNode root) {
        max(root, 1);
        return answer;
    }

    private void max(TreeNode node, int depth) {
        if (node == null) {
            return;
        }
        if (node.left == null && node.right == null) {
            answer = Math.max(answer, depth);
        }
        max(node.left, depth + 1);
        max(node.right, depth + 1);
    }
}
