#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
#define rep(i,a,b) for (ll i = a; i<ll(b); i++)
//compile with g++/cc -g -Wall -Wconversion -fsanitize=address,
//undefined <filename.cpp>
int main() {
    ios::sync_with_stdio(false);
    std::cin.tie(NULL); cout.tie(NULL);
    cout << setprecision(10);

    int testcases;
    std::cin >> testcases;
    //cout << "hello 1" << endl;

    for (int testcase = 0; testcase < testcases; testcase++){
        int n; int m;
        int pop = 0;
        int troops = 0;
        std::cin >> n >> m;
        //cout << "hello 2" << endl;
        //std::cin >> m;
        //cout << "3" << endl;
        int a[n+2][m+2];
        for (int i = 0; i < m+2; i++){
            a[0][i] = 0;
            a[n+1][i] = 0;
        }
        //cout << "hello 3" << endl;
        for (int i = 1; i < n+1; i++){
            a[i][0] = 0;
            a[i][m+1] = 0;
            for (int j = 1; j < m+1; j++){
                int tmp;
                std::cin >> tmp;
                a[i][j] = tmp;
            }
        }
        // for (int r = 0; r < n+2; r++){
        //     for (int s = 0; s < m+2; s++){
        //         cout << a[r][s] << " ";
        //     }
        //     cout << endl;
        // }
        for (int lnum = 1; lnum <= n+1; lnum++){
            for (int cnum = 1; cnum <= m+1; cnum++){
                if (not a[lnum][cnum] == 0){
                    troops++;
                    queue<pair<int, int>> q;
                    q.push(make_pair(lnum, cnum));
                    a[lnum][cnum] = 0;
                    int tpop = 0;
                    while (not q.empty()){
                        pair<int, int> v = q.front();
                        q.pop();
                        a[v.first][v.second] = 0;
                        tpop++;
                        pair<int,int> toadd[] = {
                        make_pair(v.first-1, v.second-1),
                        make_pair(v.first-1, v.second),
                        make_pair(v.first-1, v.second+1),
                        make_pair(v.first, v.second+1),
                        make_pair(v.first+1, v.second+1),
                        make_pair(v.first+1, v.second),
                        make_pair(v.first+1, v.second-1),
                        make_pair(v.first, v.second-1)};
                        for (int k = 0; k < 8; k++){
                            if (not a[toadd[k].first][toadd[k].second] == 0){
                                a[toadd[k].first][toadd[k].second] = 0;
                                q.push(toadd[k]);
                            }
                        }
                    }
                pop = max(pop, tpop);
                }
            }
        }
    cout << troops << " " << pop << endl;
    }
// int next;
// std::cin >> next;
}
