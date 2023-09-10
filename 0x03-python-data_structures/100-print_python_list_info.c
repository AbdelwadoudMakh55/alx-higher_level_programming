#include <stdio.h>
#include "Python.h"
/**
 *  print_python_list_info - prints some basic info about Python lists.
 *  @p : Pointer to a PyObject.
 *  Return: Void.
 */
void print_python_list_info(PyObject *p)
{
	int i;
	PyListObject **new_pointer;

	new_pointer = (PyListObject *)p;
	printf("[*] Size of the Python List = %u", new_pointer->ob_base.ob_size);
	printf("[*] Allocated = %u", new_pointer->allocated);
	for (i = 0; i < new_pointer->ob_base.ob_size; i++)
		printf("Element %d: %s\n", i, new_pointer->ob_item[i]->ob_type->tp_name);
}
