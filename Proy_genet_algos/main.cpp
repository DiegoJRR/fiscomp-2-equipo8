// Proyecto de algoritmo geneticos

/*Ajuste de un polinomio de orden 4 utilizando
algoritmo genetico y datos presentados en el archivo
mock_data_txt*/

#include <iostream>
#include <random>
#include <fstream>
#include <math.h>
#include <algorithm>
#include <chrono>
#include <cstdlib>
#include <iomanip>

using namespace std;

// Función que genera números aleatorios en un rango
double num_ale(double LO, double HI)
{
    // Engine para los números aleatorios
    static default_random_engine generator(chrono::steady_clock::now().time_since_epoch().count());
    // Distribución uniforme
    uniform_real_distribution<double> distribution(LO, HI);
    return distribution(generator);
}

// Vector que regresa 5 coeficientes en los rangos requeridos
vector<double> coeficientes()
{
    vector<double> x = {num_ale(-10, 10), num_ale(-10, 20), num_ale(-100, 100), num_ale(-200, 200), num_ale(-1000, 1000)};
    return x;
}

// Función de aptitud
// Primer parametro son las x de los datos, segundo las y, tercero sigma y ultimo los coeficientes a usar
double fit_func(const vector<double> &y, const vector<double> &x, const vector<double> &sigma, const vector<double> &coe)
{
    // Observamos resultados aprox del orden e-7
    // Guardar la sumatoria
    double suma = 0;
    // Ejecutamos la funcion de aptitud que tenemos para el problema
    for (int i = 0; i < x.size(); i++)
    {
        double M = coe[0] * pow(x.at(i), 4) + coe[1] * pow(x.at(i), 3) + coe[2] * pow(x.at(i), 2) + coe[3] * pow(x.at(i), 1) + coe[4];
        double func = pow(((y.at(i) - M) / sigma.at(i)), 2);
        suma = suma + func;
    }
    double final = 1 / suma;
    return final;
}

// Definimos la estructura de nuestros individuos
struct individuo
{
    // Vector con los coeficientes de cada individuo
    vector<double> coeff;
    // Valor de la función de aptitud del individuo
    double aptitud;

    // Definimos un constructor con valores predeterminados para nuestros individuos
    individuo()
    {
        // Coeficientes aleatorios asignados de acuerdo al rango establecido
        coeff = coeficientes();
    }
};

// Funcion de mutacion
// Recibe como parametro vector con dos individuos y el parametro para juzgar mutacion
vector<individuo> mutacion(vector<individuo> Indi, const double param)
{
    // Definimos numero aleatorio entre 0 y 1
    double aleatorio = num_ale(0, 1);
    // Creamos dos individuos nuevos
    individuo indi1;
    individuo indi2;
    // Igualamos coeficientes
    indi1.coeff = Indi[0].coeff;
    indi2.coeff = Indi[1].coeff;
    // Se cumple el resto si es menor al parametro
    if (aleatorio < param)
    {
        // Establecemos dos numeros aleatorios para nuestros indices
        int uno = round(num_ale(0, Indi[0].coeff.size() - 1));
        int dos = round(num_ale(0, Indi[0].coeff.size() - 1));

        // Valores donde guardar el coeficiente escogido
        double first = Indi[0].coeff.at(uno);
        double second = Indi[1].coeff.at(dos);

        // Procedemos a intercambiarlos
        Indi[0].coeff.at(uno) = second;
        Indi[1].coeff.at(dos) = first;
        return {indi1, indi2};
    }
    return {Indi[0], Indi[1]};
}

// Método ruleta
// Tomamos como parametro todo nuestro vector de poblacion, y el numero de poblacion total
individuo ruleta(const vector<individuo> &Indi, const int pobla)
{
    // Sumamos todas las aptitudes
    double sum_apt = 0;
    for (int i = 0; i < pobla; i++)
    {
        sum_apt = sum_apt + Indi.at(i).aptitud;
    }
    // Genereamos dos numeros aleatorios para encontrar a los dos individuos
    double aleatorio1 = num_ale(0, sum_apt);
    // Hacemos suma parcial hasta encontrar aptitud mayor a este
    double sum_parcial1 = 0;
    int h;
    // Inicializamos los individuos que vamos a obtener de la ruleta
    individuo indi1;
    for (h = 0; h < pobla; h++)
    {
        sum_parcial1 = sum_parcial1 + Indi.at(h).aptitud;
        if (sum_parcial1 > aleatorio1)
        {
            break;
        }
    }

    /*cout <<"Numero aleatorio" << endl;
    cout << aleatorio1 <<endl;
    cout <<"Suma total aptitud" << endl;
    cout << sum_apt << endl;
    cout << "Suma parcial" << endl;
    cout << sum_parcial1 << endl;
    cout <<"Vienen las h" << endl;
    cout << h <<endl;
    indi1.coeff = Indi.at(h).coeff;
    indi1.aptitud = Indi.at(h).aptitud;
    cout << indi1.aptitud << endl; */

    return indi1;
}

// Funcion de cruzamiento
// Ingresas como parametro vector con ambos individuos y punto de cruzamiento
// Te regresa vector de dos individuos cruzados
vector<individuo> cruzamiento(const vector<individuo> &padres, const int punto)
{
    // Inicializamos los individuos donde pondremo nuestros hijos
    individuo hijo1;
    individuo hijo2;
    // LLenamos la primera parte de los vectores
    for (int i = 0; i < punto; i++)
    {
        hijo1.coeff.at(i) = padres.at(0).coeff.at(i);
        hijo2.coeff.at(i) = padres.at(1).coeff.at(i);
    }
    // Terminamos de llenar con vectores cruzados
    for (int i = punto; i < padres.at(0).coeff.size(); i++)
    {
        hijo1.coeff.at(i) = padres.at(1).coeff.at(i);
        hijo2.coeff.at(i) = padres.at(0).coeff.at(i);
    }
    return {hijo1, hijo2};
}

// Funcion para comparar aptitud entre individuos
bool compare(const individuo &x, const individuo &y)
{
    return x.aptitud < y.aptitud;
}

// Funcion de sacrificio
// Parametros toma como parametros a la poblacion& para borrar directamente
// Ya que esta sorteado de forma descendente solo tenemos que eliminar los últimos individuos
void matar(vector<individuo> &Indi)
{
    for (int i = 0; i < 2; i++)
    {
        Indi.erase(min_element(Indi.begin(), Indi.end(), compare));
    }
}

int main()
{
    cout << "Inicio de programa" << endl;

    // Población inicial
    const int num_poblacion = 50;
    // Punto de cruzamiento entre individuos
    const int punto_cruz = 2;
    // Paramatro de mutacion
    const double para_mutacion = 0.1;
    // Vector del numero de iteraciones dados
    const int iteraciones = 1000;
    // Vector para guardar la mejor aptitud al final
    vector<individuo> best_apti;
    cout << setprecision(15);

    // Vectores donde guardaremos los datos del archivo
    vector<double> x, y, sigma;
    // Leemos los datos de nuestro archivo
    ifstream indata;
    indata.open("mock_data_ga.txt");
    if (!indata)
    { // file couldn't be opened
        cerr << "Error: No se pudo abrir archivo" << endl;
        exit(1);
    }
    // Variable donde obtener los datos
    double kk = 0;
    while (!indata.eof())
    {
        // Despues de guardar el dato en kk lo introducimos a su respectivo vector
        indata >> kk;
        x.push_back(kk);
        indata >> kk;
        y.push_back(kk);
        indata >> kk;
        sigma.push_back(kk);
    }
    indata.close();

    // Inicializamos vector de poblacion
    vector<individuo> poblacion;
    // Creamos a los individuos de nuestra poblacion
    for (int i = 0; i < num_poblacion; i++)
    {
        poblacion.push_back(individuo());
        // Le asignamos la aptitud calculando de acuerdo a sus valores de coeficientes
        poblacion.at(i).aptitud = fit_func(y, x, sigma, poblacion.at(i).coeff);
    }
    // Ordenamos nuestro vector de forma que los más aptos vayan primero
    // sort(poblacion.begin(),poblacion.end(),compare);

    // Aplicamos el for por el numero de iteraciones
    for (int j = 0; j < iteraciones; j++)
    {
        // cout << j << endl;

        // Aplicamos la funcion para ver que vectores se van a cruzar
        vector<individuo> vec_ruleta;
        vec_ruleta.push_back(ruleta(poblacion, num_poblacion));
        vec_ruleta.push_back(ruleta(poblacion, num_poblacion));

        /*cout <<"Padre 1" << endl;
        for(int m = 0;m < vec_ruleta[0].coeff.size();m++){
            cout << vec_ruleta[0].coeff[m] << endl;
        }
        cout << vec_ruleta[0].aptitud << endl;
                            cout <<"Padre 2" << endl;
        for(int m = 0;m < vec_ruleta[1].coeff.size();m++){
            cout << vec_ruleta[1].coeff[m] << endl;
        }
        cout << vec_ruleta[1].aptitud << endl; */

        // Realizamos el cruzamiento de los vectores elegidos
        vector<individuo> vec_cruzar = cruzamiento(vec_ruleta, punto_cruz);
        // Aplicamos función de mutación si es que ocurre
        vector<individuo> vec_muta = mutacion(vec_cruzar, para_mutacion);

        // Calculamos la funcion de aptitud de los hijos
        vec_muta.at(0).aptitud = fit_func(y, x, sigma, vec_muta[0].coeff);
        vec_muta.at(1).aptitud = fit_func(y, x, sigma, vec_muta[1].coeff);
        // Eliminamos a los individuos más debiles
        matar(poblacion);

        // Agregamos los nuevos inviduos que creamos
        poblacion.push_back(vec_muta.at(0));
        poblacion.push_back(vec_muta.at(1));

        // Acomodamos nuestro vector de nuevo
        // sort(poblacion.begin(),poblacion.end(),compare);

        /*cout << "Aptitudes" << endl;
    for(int g = 0; g< poblacion.size();g++){
        cout << poblacion[g].aptitud << endl;
    }*/
        // Vaciamos vectores que utilizamos
        vec_ruleta.clear();
        vec_cruzar.clear();
        vec_muta.clear();
    }
    // Agregamos la aptitud del primer individuo que es la mejor
    best_apti.push_back(*max_element(poblacion.begin(), poblacion.end(), compare));
    cout << "Aptitud" << endl;
    cout << best_apti[0].aptitud << endl;
    cout << "Coeficientes" << endl;
    cout << best_apti[0].coeff[0] << endl;
    cout << best_apti[0].coeff[1] << endl;
    cout << best_apti[0].coeff[2] << endl;
    cout << best_apti[0].coeff[3] << endl;
    cout << best_apti[0].coeff[4] << endl;

    return 0;
}