// O grafo vai ser representado em uma matriz de adj
//
#include <stdlib.h>
#include <iostream>


using namespace std;
int mco;
int* vmco;
class Grafo{
private:
    int ** matAdj;
    int nvertices;
public:
    Grafo(int vertices);
    void imprimeMat();
    int insereAresta(int v1, int v2, int p);
    int existeAresta(int v1, int v2);
    int getNV();
};

Grafo::Grafo(int vertices){
    this->nvertices = vertices;
    this->matAdj = (int**)malloc(vertices*sizeof(int*));
    for(int i = 0; i < vertices; i++){
        this->matAdj[i] = (int *)malloc(vertices*sizeof(int));
    }
    for(int i = 0; i < vertices; i++){
        for(int j = 0; j < vertices; j++){
            this->matAdj[i][j] = 0;
        }
    }
}

void Grafo::imprimeMat(){
    for(int i = 0; i < this->nvertices; i++){
        for(int j = 0; j < this->nvertices; j++){
            cout << this->matAdj[i][j] << '\t';            
        }
        cout << endl;
    }
}

int Grafo::insereAresta(int v1, int v2, int p){
    this->matAdj[v1][v2] = p;
    this->matAdj[v2][v1] = p;
}

int Grafo::existeAresta(int v1, int v2){
    // cout << "v1:" << v1 << "\t";
    // cout << "v2:" << v2 << "\t";
    // cout << "mat:" << matAdj[v1][v2] << endl;
    return matAdj[v1][v2];
}

int Grafo::getNV(){
    return this->nvertices;
}

int calc_caminho(int *vet, int nv, Grafo *g){
    int dist = 0;
    int i;
    int aux;
    for(i =1;i < nv;i++){
        if(aux = g->existeAresta(vet[i-1],vet[i])){
            dist += aux;
        } else{
            return -1;
        }
    }
    if(aux = g->existeAresta(vet[nv-1],vet[0])){
        dist += aux;
    } else{
        return -1;
    }
    return dist;
}

int permuta(int *vet, int n, int nv, Grafo* g){
    int aux;
    if(n == nv){
        int d = calc_caminho(vet,nv,g);
        
        if(d > 0 && d < mco){
            mco = d;
            for(int i = 0; i<nv;i++){
                vmco[i] = vet[i];
            }
        }
        if(d > 0){
            cout << d << endl;
            for(int i = 0; i<nv;i++){
                cout << vet[i] << "\t";
            }   
            cout << endl;
        }
    } else{
        for(int i=n; i<nv;i++){
            aux = vet[n];
            vet[n] = vet[i];
            vet[i] = aux;
            permuta(vet,n+1,nv,g);
            aux = vet[n];
            vet[n] = vet[i];
            vet[i] = aux;
        }
    }
}

int PCV_otimo(Grafo* g){
    int nv = g->getNV();
    int * vet = (int*)malloc(nv * sizeof(int));
    vmco = (int*)malloc(nv * sizeof(int));
    for(int i = 0; i < nv; i++)
        vet[i] = i;
    mco = 99999999;

    permuta(vet,0,nv,g);
}

int main(){
    FILE * pFile;
    pFile = fopen("grafo-ex.txt", "r");
    char buffer[100];
    int primeiroLinha = 1;
    int nv,v1,v2,p;
    Grafo* g;
    if(pFile == NULL) perror ("Error opening file");
    else{
        while(! feof(pFile)){
            if(primeiroLinha){
                fscanf(pFile, "%d", &nv);
                g = new Grafo(nv);
                primeiroLinha = 0;
            } else{
                if(fscanf(pFile, "%d %d %d", &v1, &v2, &p) == -1) break;
                g->insereAresta(v1,v2,p);
            }
        }
        fclose(pFile);
    }
    
    PCV_otimo(g);
    cout << mco << endl;
    for(int i = 0; i< g->getNV();i++){
        cout << vmco[i] << "\t";
    }
    cout << endl;
    //g->imprimeMat();
    return 0;
}