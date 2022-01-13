package rv0010.binarytree.traversal;

import rv0010.binarytree.TreeNode;

import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

public class InorderTraversal implements DFSTraversable {

    public List<Integer> recursiveTraversal(TreeNode root) {
        List<Integer> treeElems = new ArrayList<>();
        if (root == null) return treeElems;
        treeElems.addAll(recursiveTraversal(root.getLeft()));
        treeElems.add(root.getVal());
        treeElems.addAll(recursiveTraversal(root.getRight()));
        return treeElems;
    }

    public List<Integer> iterativeTraversal(TreeNode root) {
        List<Integer> treeElems = new ArrayList<>();
        if (root == null) return treeElems;
        Stack<TreeNode> nodeStack = new Stack<>();
        TreeNode curr = root;
        while (curr != null || !nodeStack.isEmpty()) {
            while (curr != null) {
                nodeStack.push(curr);
                curr = curr.getLeft();
            }
            TreeNode node = nodeStack.pop();
            treeElems.add(node.getVal());
            curr = node.getRight();
        }
        return treeElems;
    }


}
