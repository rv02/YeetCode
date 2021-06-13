package rv0010.binarytree;

import rv0010.binarytree.traversal.*;
import rv0010.binarytree.construct.*;

public class Main {

    public static void main(String[] args) {
        DFSTraversable obj = new PreOrder();
        DFSTraversable in = new InorderTraversal();
        DFSTraversable p = new PostOrderTraversal();
        MaxDepth depth = new MaxDepth();
        Symmetric symObj = new Symmetric();
        TreeNode left = new TreeNode(1);
        TreeNode right = new TreeNode(1);
        TreeNode parent = new TreeNode(3, left, right);
        System.out.println(LevelOrder.levelOrder(parent));
        // System.out.println(depth.maxDepth(parent));
        System.out.println(symObj.isSymmetric(parent));
    }


}
