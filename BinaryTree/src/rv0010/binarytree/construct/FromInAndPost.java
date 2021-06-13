package rv0010.binarytree.construct;

import rv0010.binarytree.TreeNode;

class FromInAndPost {
    private int index;

    public TreeNode buildTree(int[] inorder, int[] postorder) {
        int n = inorder.length;
        index = n - 1;
        return build(inorder, postorder, 0, n - 1);
    }

    private TreeNode build(int[] inorder, int[] postorder, int inStart, int inEnd) {
        if (inStart > inEnd) {
            return null;
        }
        TreeNode node = new TreeNode(postorder[index]);
        index--;
        if(inStart == inEnd) {
            return node;
        }
        int search = linearSearch(inorder, inStart, inEnd,node.getVal());
        node.setRight(build(inorder, postorder, search + 1, inEnd));
        node.setLeft(build(inorder, postorder, inStart, search - 1));
        return node;
    }

    private int linearSearch(int[] array, int start, int end,int val) {
        for (int i = start; i <= end; i++) {
            if (array[i] == val) {
                return i;
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        FromInAndPost obj = new FromInAndPost();
        TreeNode root = obj.buildTree(new int[]{4, 8, 2, 5, 1, 6, 3, 7},
                new int[]{8, 4, 5, 2, 6, 7, 3, 1});
    }
}
