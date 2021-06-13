package rv0010.binarytree.traversal;

import rv0010.binarytree.TreeNode;

import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

public class PostOrderTraversal implements DFSTraversable {

    public List<Integer> recursiveTraversal(TreeNode root) {
        List<Integer> treeElems = new ArrayList<>();
        if (root == null) return treeElems;
        treeElems.addAll(recursiveTraversal(root.getLeft()));
        treeElems.addAll(recursiveTraversal(root.getRight()));
        treeElems.add(root.getVal());
        return treeElems;
    }

    public List<Integer> iterativeTraversal(TreeNode root) {
        List<Integer> treeElems = new ArrayList<>();
        if (root == null) return treeElems;
        Stack<TreeNode> nodeStack1 = new Stack<>();
        Stack<TreeNode> nodeStack2 = new Stack<>();
        nodeStack1.push(root);
        while (!nodeStack1.isEmpty()) {
            TreeNode node = nodeStack1.pop();
            nodeStack2.push(node);
            if (node.getLeft() != null) nodeStack1.push(node.getLeft());
            if (node.getRight() !=  null) nodeStack1.push(node.getRight());
        }
        while (!nodeStack2.isEmpty()) {
            treeElems.add(nodeStack2.pop().getVal());
        }
        return treeElems;
    }
}
