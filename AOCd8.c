#include<2D_matrix_ops.h>

matrix * rotate_column(matrix * x, int c, int cm);
matrix * rotate_row(matrix * x, int r, int am);
matrix * rec(matrix * x, int a, int b);
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

