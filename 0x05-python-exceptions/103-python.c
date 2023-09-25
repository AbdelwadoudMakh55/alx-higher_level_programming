#include "Python.h"
/**
 *  print_python_list_info - prints some basic info about Python lists.
 *  @p : Pointer to a PyObject.
 *  Return: Void.
 */
void print_python_float(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_list(PyObject *p)
{
	long int i;
	PyListObject *new;
	
        if (!PyList_Check(p))
        {
                printf("[.] Python list info\n");
                printf("  [ERROR] Invalid List Object\n");
                return;
        }
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", PyList_Size(p));
	new = (PyListObject *)p;
	printf("[*] Allocated = %ld\n", new->allocated);
	for (i = 0; i < PyList_Size(p); i++)
	{
		printf("Element %ld: %s\n", i, new->ob_item[i]->ob_type->tp_name);
		if (new->ob_item[i]->ob_type->tp_name[0] ==  'b')
			print_python_bytes((PyObject *)new->ob_item[i]);
		if (new->ob_item[i]->ob_type->tp_name[0] ==  'f')
			print_python_float((PyObject *)new->ob_item[i]);
	}
}
/**
 * print_python_bytes - print some basic info about Python bytes objects.
 * @p : Pointer to PyObject.
 * Return: Void.
 */
void print_python_bytes(PyObject *p)
{
	long int i;

	if (!PyBytes_Check(p))
	{
		printf("[.] bytes object info\n");
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	printf("[.] bytes object info\n");
	printf("  size: %ld\n", PyBytes_Size(p));
	printf("  trying string: %s\n",PyBytes_AsString(p));
	if (PyBytes_Size(p) < 10)
	{
		printf("  first %ld bytes:", PyBytes_Size(p) + 1);
		for (i = 0; i < PyBytes_Size(p) + 1; i++)
			printf(" %02x", PyBytes_AsString(p)[i]);
		printf("\n");
	}
	else
	{
		printf("  first 10 bytes:");
		for (i = 0; i < 10; i++)
			printf(" %02x", PyBytes_AsString(p)[i]);
		printf("\n");
	}
}
/**
 * print_python_float - print some basic info about Python floats objects.
 * @p : Pointer to PyObject.
 * Return: Void.
 */
void print_python_float(PyObject *p)
{
	if (!PyFloat_Check(p))
	{
		printf("[.] float object info\n");
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
	printf("[.] float object info\n");
	printf("  value: %lf\n", PyFloat_AsDouble(p));

