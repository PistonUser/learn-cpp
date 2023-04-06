#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main () {
  // Create a text string, which is used to output the text file
  string myText;

  // Read from the text file
  ifstream MyReadFile("filename.txt");

  // Use a while loop together with the getline() function to read the file line by line
  getline (MyReadFile, myText);
    // Output the text from the file
  cout << myText << " next line\n";
  

  // Close the file
  MyReadFile.close();
}
