from collections import defaultdict, deque

# -------------- LCA 相關函式 --------------
def build_tree(lines):
    n = int(lines[0])
    w1, w2 = map(int, lines[1].split())

    children = defaultdict(list)
    parent = dict()
    all_nodes = set()

    # 建立樹結構
    for line in lines[2:]:
        parts = list(map(int, line.split()))
        parent_node = parts[0]
        all_nodes.add(parent_node)

        for child_node in parts[1:]:
            children[parent_node].append(child_node)
            parent[child_node] = parent_node
            all_nodes.add(child_node)

    # 找根節點
    root = None
    for node in all_nodes:
        if node not in parent:
            root = node
            break

    return n, w1, w2, children, parent, root

def bfs_depth(root, children):
    depth = {root: 0}
    parent_up = {root: None}
    q = deque([root])

    while q:
        current = q.popleft()
        for child in children[current]:
            depth[child] = depth[current] + 1
            parent_up[child] = current
            q.append(child)

    return depth, parent_up

def get_lca(u, v, depth, parent_up):
    # 調整到同一深度
    while depth[u] > depth[v]:
        u = parent_up[u]
    while depth[v] > depth[u]:
        v = parent_up[v]
    
    # 一起往上跳
    while u != v:
        u = parent_up[u]
        v = parent_up[v]
    return u

# -------------- 主程式 --------------
def main():
    blocks = []
    current_block = []

    # 逐行讀，遇到空行分割區塊
    while True:
        try:
            line = input().strip()
            if not line:
                if current_block:
                    blocks.append(current_block)
                    current_block = []
                continue
            current_block.append(line)
        except EOFError:
            if current_block:
                blocks.append(current_block)
            break

    # 處理每一個區塊（每一組測資）
    for block in blocks:
        n, w1, w2, children, parent, root = build_tree(block)
        depth, parent_up = bfs_depth(root, children)
        ancestor = get_lca(w1, w2, depth, parent_up)
        
        # 計算最終距離
        distance = depth[w1] + depth[w2] - 2 * depth[ancestor]
        print(distance)

if __name__ == "__main__":
    main()