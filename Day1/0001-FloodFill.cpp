class Solution {
public:
    void dfs(vector<vector<int>>& image, int x, int y, int oldco, int newco){
        if(x<0 || x >= image.size() || y < 0 || y >= image[0].size()|| image[x][y] != oldco){
            return;
        }
        image[x][y] = newco;
        dfs(image, x+1, y, oldco, newco);
        dfs(image, x-1, y, oldco, newco);
        dfs(image, x, y+1, oldco, newco);
        dfs(image, x, y-1, oldco, newco);
    }
    vector<vector<int>> floodFill(vector<vector<int>>& image, int sr, int sc, int color) {
        int oldco = image[sr][sc];
        if (oldco != color){
            dfs(image, sr,sc, oldco, color);
        }
        return image;
    }
};
