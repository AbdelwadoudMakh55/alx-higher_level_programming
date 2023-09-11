#include <stdio.h>
#include <Python.h>
/**
 *  print_python_list_info - prints some basic info about Python lists.
 *  @p : Pointer to a PyObject.
 *  Return: Void.
 */
void print_python_list_info(PyObject *p)
{
	long int i;
	PyListObject *new;

	printf("[*] Size of the Python List = %ld\n", PyList_Size(p));
	new = (PyListObject *)p;
	printf("[*] Allocated = %ld\n", new->allocated);
	for (i = 0; i < PyList_Size(p); i++)
		printf("Element %ld: %s\n", i, new->ob_item[i]->ob_type->tp_name);
}
