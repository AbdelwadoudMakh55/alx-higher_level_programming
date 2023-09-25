#include "Python.h"
/**
 *  print_python_list_info - prints some basic info about Python lists.
 *  @p : Pointer to a PyObject.
 *  Return: Void.
 */
void print_python_list(PyObject *p)
{
	long int i;
	PyListObject *new;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", PyList_Size(p));
	new = (PyListObject *)p;
	printf("[*] Allocated = %ld\n", new->allocated);
	for (i = 0; i < PyList_Size(p); i++)
		printf("Element %ld: %s\n", i, new->ob_item[i]->ob_type->tp_name);
}
/**
 * print_python_bytes - print some basic info about Python bytes objects.
 * @p : Pointer to PyObject.
 * Return: Void.
 */
void print_python_bytes(PyObject *p)
{

	printf("[.] bytes object info\n");
	printf("size: %ld\n", PyBytes_Size(p));
	/*printf("trying string: %s\n", );
	printf("first %ld bytes: \n", );*/
}
