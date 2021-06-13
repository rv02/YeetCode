package rv0010.binarytree;

class Symmetric {
    public boolean isSymmetric(TreeNode root) {
        return symmetry(root, root);
    }

    private boolean symmetry(TreeNode node1, TreeNode node2) {
        if (node1 == null && node2 == null) {
            return true;
        } else if (node1 == null || node2 == null) {
            return false;
        }
        return node1.val == node2.val &&
        symmetry(node1.left, node2.right) &&
        symmetry(node1.right, node2.left);
    }
}
