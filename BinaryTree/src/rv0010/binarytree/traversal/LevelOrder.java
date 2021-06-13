package rv0010.binarytree.traversal;

import rv0010.binarytree.TreeNode;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

public class LevelOrder {
    public static List<List<Integer>> levelOrder(TreeNode root) {
        Queue<TreeNode> nodes = new LinkedList<>();
        List<List<Integer>> tree = new ArrayList<>();
        nodes.add(root);
        int i = (root == null)?0:1;
        while(i != 0) {
            int levelCount = 0;
            tree.add(new ArrayList<>());
            for (int j = 0; j < i; j++) {
                TreeNode curr = nodes.remove();
                if (curr.getLeft() != null) {
                    nodes.add(curr.getLeft());
                    levelCount++;
                }
                if (curr.getRight() != null) {
                    nodes.add(curr.getRight());
                    levelCount++;
                }
                tree.get(tree.size() - 1).add(curr.getVal());
            }
            i = levelCount;
        }
        return tree;
    }
}
