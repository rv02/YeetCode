package rv0010.binarytree.traversal;

import rv0010.binarytree.TreeNode;

import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

public class PreOrder implements DFSTraversable{

    public List<Integer> recursiveTraversal(TreeNode root) {
        List<Integer> treeElems = new ArrayList<>();
        if (root == null) return treeElems;
        treeElems.add(root.getVal());
        treeElems.addAll(recursiveTraversal(root.getLeft()));
        treeElems.addAll(recursiveTraversal(root.getRight()));
        return treeElems;
    }

    public List<Integer> iterativeTraversal(TreeNode root) {
        List<Integer> treeElems = new ArrayList<>();
        if (root == null) return treeElems;
        Stack<TreeNode> nodeStack = new Stack<>();
        nodeStack.push(root);
        while(!nodeStack.isEmpty()) {
            TreeNode node = nodeStack.peek();
            nodeStack.pop();
            treeElems.add(node.getVal());
            if (node.getRight() != null)
                nodeStack.push(node.getRight());
            if (node.getLeft() != null)
                nodeStack.push(node.getLeft());
        }
        return treeElems;
    }
}
