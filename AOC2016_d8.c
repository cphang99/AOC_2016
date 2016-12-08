#include<2D_matrix_ops.h>

matrix * rotate_column(matrix * x, int c, int cm);
matrix * rotate_row(matrix * x, int r, int am);
matrix * rec(matrix * x, int a, int b);
int t1(void);
int count(matrix * a);
int main(void) {
    matrix * a = initialise_matrix(3, 7);
    rec(a, 3,2);
    print_matrix(a);
    rotate_column(a, 1, 1);
    print_matrix(a);
    rotate_row(a, 0, 4);
    print_matrix(a);
    rotate_column(a, 1, 1);
    print_matrix(a);
    count(a);
    destroy_matrix(&a);
    t1();
}

matrix * rec(matrix * x, int a, int b) {
    for(int i = 0; i < b; i++) {
        for(int j = 0; j < a; j++) {
            set_matrix_member(x, i+1, j+1, 1);
        }
    }
    return x;
}

matrix * rotate_row(matrix * x, int r, int am) {
    matrix * row = get_horizontal_slice(x, r+1, r+1);
    for(int i = 0; i < get_columns(x); i++) {
        int index = (i+am) % get_columns(x);
        set_matrix_member(x, r+1, index+1, 
                get_matrix_member(row, 1, i+1));
    }
    destroy_matrix(&row);
    return x;
}

matrix * rotate_column(matrix * x, int c, int cm) {
    matrix * col = get_vertical_slice(x, c+1, c+1);
    for(int i = 0; i < get_rows(x); i++) {
        int index = (i + cm) % get_rows(x);
        set_matrix_member(x, index+1, c+1,
                get_matrix_member(col, i+1, 1));
    }
    destroy_matrix(&col);
    return x;
}

int count(matrix * a) {
    int count = 0;
    for(int i = 0; i < get_rows(a); i++) {
        for(int j=0; j < get_columns(a); j++) {
            if(get_matrix_member(a, i+1, j+1)) count++;
        }
    }
    printf("Number of pixels lit = %d\n", count);
    return count;
}

int t1(void) {
    matrix * a = initialise_matrix(6, 50);
    rec(a, 1, 1);
    rotate_row(a, 0, 7);
    rec(a, 1, 1);
    rotate_row(a, 0, 5);
    rec(a, 1, 1);
    rotate_row(a, 0, 5);
    rec(a, 1, 1);
    rotate_row(a, 0, 2);
    rec(a, 1, 1);
    rotate_row(a, 0, 3);
    rec(a, 1, 1);
    rotate_row(a, 0, 5);
    rec(a, 1, 1);
    rotate_row(a, 0, 3);
    rec(a, 1, 1);
    rotate_row(a, 0, 2);
    rec(a, 1, 1);
    rotate_row(a, 0, 3);
    rec(a, 2, 1);
    rotate_row(a, 0, 7);
    rec(a, 6, 1);
    rotate_row(a, 0, 3);
    rec(a, 2, 1);
    rotate_row(a, 0, 2);
    rec(a, 1, 2);
    rotate_row(a, 1, 10);
    rotate_row(a, 0, 3);
    rotate_column(a, 0, 1);
    rec(a, 2, 1);
    rotate_column(a, 20, 1);
    rotate_column(a, 15, 1);
    rotate_column(a, 5, 1);
    rotate_row(a, 1, 5);
    rotate_row(a, 0, 2);
    rec(a, 1, 2);
    rotate_row(a, 0, 5);
    rotate_column(a, 0, 1);
    rec(a, 4, 1);
    rotate_row(a, 2, 15);
    rotate_row(a, 0, 5);
    rotate_column(a, 0, 1);
    rec(a, 4, 1);
    rotate_row(a, 2, 5);
    rotate_row(a, 0, 5);
    rotate_column(a, 0, 1);
    rec(a, 4, 1);
    rotate_row(a, 2, 10);
    rotate_row(a, 0, 10);
    rotate_column(a, 8, 1);
    rotate_column(a, 5, 1);
    rotate_column(a, 0, 1);
    rec(a, 9, 1);;
    rotate_column(a, 27, 1);
    rotate_row(a, 0, 5);
    rotate_column(a, 0, 1);
    rec(a, 4, 1);
    rotate_column(a, 42, 1);
    rotate_column(a, 40, 1);
    rotate_column(a, 22, 1);
    rotate_column(a, 17, 1);
    rotate_column(a, 12, 1);
    rotate_column(a, 7, 1);
    rotate_column(a, 2, 1);
    rotate_row(a, 3, 10);
    rotate_row(a, 2, 5);
    rotate_row(a, 1, 3);
    rotate_row(a, 0, 10);
    rec(a, 1, 4);
    rotate_column(a, 37, 2);
    rotate_row(a, 3, 18);
    rotate_row(a, 2, 30);
    rotate_row(a, 1, 7);
    rotate_row(a, 0, 2);
    rotate_column(a, 13, 3);
    rotate_column(a, 12, 1);
    rotate_column(a, 10, 1);
    rotate_column(a, 7, 1);
    rotate_column(a, 6, 3);
    rotate_column(a, 5, 1);
    rotate_column(a, 3, 3);
    rotate_column(a, 2, 1);
    rotate_column(a, 0, 1);
    rec(a, 14, 1);
    rotate_column(a, 38, 3);
    rotate_row(a, 3, 12);
    rotate_row(a, 2, 10);
    rotate_row(a, 0, 10);
    rotate_column(a, 7, 1);
    rotate_column(a, 5, 1);
    rotate_column(a, 2, 1);
    rotate_column(a, 0, 1);
    rec(a, 9, 1);
    rotate_row(a, 4, 20);
    rotate_row(a, 3, 25);
    rotate_row(a, 2, 10);
    rotate_row(a, 0, 15);
    rotate_column(a, 12, 1);
    rotate_column(a, 10, 1);
    rotate_column(a, 8, 3);
    rotate_column(a, 7, 1);
    rotate_column(a, 5, 1);
    rotate_column(a, 3, 3);
    rotate_column(a, 2, 1);
    rotate_column(a, 0, 1);
    rec(a, 14, 1);
    rotate_column(a, 34, 1);
    rotate_row(a, 1, 45);
    rotate_column(a, 47, 1);
    rotate_column(a, 42, 1);
    rotate_column(a, 19, 1);
    rotate_column(a, 9, 2);
    rotate_row(a, 4, 7);
    rotate_row(a, 3, 20);
    rotate_row(a, 0, 7);
    rotate_column(a, 5, 1);
    rotate_column(a, 3, 1);
    rotate_column(a, 2, 1);
    rotate_column(a, 0, 1);
    rec(a, 6, 1);
    rotate_row(a, 4, 8);
    rotate_row(a, 3, 5);
    rotate_row(a, 1, 5);
    rotate_column(a, 5, 1);
    rotate_column(a, 4, 1);
    rotate_column(a, 3, 2);
    rotate_column(a, 2, 1);
    rotate_column(a, 1, 3);
    rotate_column(a, 0, 1);
    rec(a, 6, 1);
    rotate_column(a, 36, 3);
    rotate_column(a, 25, 3);
    rotate_column(a, 18, 3);
    rotate_column(a, 11, 3);
    rotate_column(a, 3, 4);
    rotate_row(a, 4, 5);
    rotate_row(a, 3, 5);
    rotate_row(a, 2, 8);
    rotate_row(a, 1, 8);
    rotate_row(a, 0, 3);
    rotate_column(a, 3, 4);
    rotate_column(a, 0, 4);
    rec(a, 4, 4);
    rotate_row(a, 4, 10);
    rotate_row(a, 3, 20);
    rotate_row(a, 1, 10);
    rotate_row(a, 0, 10);
    rotate_column(a, 8, 1);
    rotate_column(a, 7, 1);
    rotate_column(a, 6, 1);
    rotate_column(a, 5, 1);
    rotate_column(a, 3, 1);
    rotate_column(a, 2, 1);
    rotate_column(a, 1, 1);
    rotate_column(a, 0, 1);
    rec(a, 9, 1);
    rotate_row(a, 0, 40);
    rotate_column(a, 44, 1);
    rotate_column(a, 35, 5);
    rotate_column(a, 18, 5);
    rotate_column(a, 15, 3);
    rotate_column(a, 10, 5);
    rotate_row(a, 5, 15);
    rotate_row(a, 4, 10);
    rotate_row(a, 3, 40);
    rotate_row(a, 2, 20);
    rotate_row(a, 1, 45);
    rotate_row(a, 0, 35);
    rotate_column(a, 48, 1);
    rotate_column(a, 47, 5);
    rotate_column(a, 46, 5);
    rotate_column(a, 45, 1);
    rotate_column(a, 43, 1);
    rotate_column(a, 40, 1);
    rotate_column(a, 38, 2);
    rotate_column(a, 37, 3);
    rotate_column(a, 36, 2);
    rotate_column(a, 32, 2);
    rotate_column(a, 31, 2);
    rotate_column(a, 28, 1);
    rotate_column(a, 23, 3);
    rotate_column(a, 22, 3);
    rotate_column(a, 21, 5);
    rotate_column(a, 20, 1);
    rotate_column(a, 18, 1);
    rotate_column(a, 17, 3);
    rotate_column(a, 13, 1);
    rotate_column(a, 10, 1);
    rotate_column(a, 8, 1);
    rotate_column(a, 7, 5);
    rotate_column(a, 6, 5);
    rotate_column(a, 5, 1);
    rotate_column(a, 3, 5);
    rotate_column(a, 2, 5);
    rotate_column(a, 1, 5);

    int c = count(a);
    print_matrix(a);
    destroy_matrix(&a);
    return c;
}
