package rv0010.binarytree.traversal;

import rv0010.binarytree.TreeNode;

import java.util.List;

public interface DFSTraversable {
    List<Integer> recursiveTraversal(TreeNode root);
    List<Integer> iterativeTraversal(TreeNode root);
}
