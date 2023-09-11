#include <stdio.h>
#include "Python.h"
/**
 *  print_python_list_info - prints some basic info about Python lists.
 *  @p : Pointer to a PyObject.
 *  Return: Void.
 */
void print_python_list_info(PyObject *p)
{
/*	int i;*/

	printf("[*] Size of the Python List = %ld\n", PyList_Size(p));
	/*printf("[*] Allocated = %ld\n", p->allocated);
	for (i = 0; i < p->ob_size; i++)
		printf("Element %d: %s\n", i, p->ob_item[i]);*/
}
