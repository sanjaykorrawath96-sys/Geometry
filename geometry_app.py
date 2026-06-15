import streamlit as st
import time

def triangle_perimeter(a,b,c):
    return a+b+c

def triangle_area(a,b,c):
    s = (a+b+c)/2
    area = (s*(s-a)*(s-b)*(s-c))**(1/2)
    return area

def square_perimeter(side):
    return 4*side

def square_area(side):
    return side**2

def rectangle_perimeter(l,b):
    return 2*(l+b)

def area_rectangle(l,b):
    return l*b

def circle_perimeter(r):
    return 2*(22/7)*r

def area_circle(r):
    return (22/7)*(r**2)


# 3D objects

def cone_tsa(r,l):
    return ((22/7)*r*(r+l))

def cone_vol(r,l):
    return (1/3)*(22/7)*(r**2)*((l**2)-(r**2))**(1/2)

def cube_tsa(s):
    return 6*(s**2)

def cube_vol(s):
    return s**3

def cuboid_tsa(l,b,h):
    return 2*(l*b+b*h+h*l)

def cuboid_vol(l,b,h):
    return l*b*h

def sphere_tsa(r):
    return 4*(22/7)*r*(r**2)

def sphere_vol(r):
    return (4 / 3) * (22 / 7) * (r ** 3)


def cylinder_tsa(r,h):
    return (22/7)*2*r*(h+r)

def cylinder_vol(r,h):
    return (22/7)*(r**2)*h



st.title('Geometry Calculator')

st.header('2D shapes')

st.subheader('Triangle')

col1,col2 = st.columns([1,3])

with col1:
    a = st.number_input('side1: ',key ='tri_a')
    b = st.number_input('side2: ',key = 'tri_b')
    c = st.number_input('side3: ',key = 'tri_c')

cola,colb = st.columns(2)
with cola:
    st.metric('Perimeter', triangle_perimeter(a,b,c))

with colb:
    st.metric('Area',round(triangle_area(a,b,c)))

####################################square############################
st.divider()
st.subheader('Square')

col1s,col2s = st.columns([1,3])

with col1s:
   s = st.number_input('side: ',key = 'sq_s')

colas,colbs = st.columns(2)

with colas:
    st.metric('Perimeter',square_perimeter(s))

with colbs:
    st.metric('Area',square_area(s))

##############################rectangle######################################

st.divider()
st.subheader('Rectangle')

col1r,col2r = st.columns([1,3])

with col1r:
   l = st.number_input('length: ',key = 'rec_l')
   b = st.number_input('breadth: ',key='rec_b')

colar,colbr = st.columns(2)

with colar:
    st.metric('Perimeter',rectangle_perimeter(l,b))

with colbr:
    st.metric('Area',area_rectangle(l,b))

##################################circle######################

st.divider()
st.subheader('Circle')

col1c,col2c = st.columns([1,3])

with col1c:
   r = st.number_input('radius: ',key ='cir_r')

colac,colbc = st.columns(2)

with colac:
    st.metric('Perimeter',round(circle_perimeter(r)))

with colbc:
    st.metric('Area',round(area_circle(r)))


##########################################3D objects#########################
st.divider()
st.divider()

st.header('3D Objects')

st.subheader('Cone')

col1co,col2co = st.columns([1,3])

with col1co:
    r_cone = st.number_input('radius: ',key='r_cone')
    l_cone = st.number_input('lateral side length: ',key ='l_cone')

colaco,colbco = st.columns(2)

with colaco:
    st.metric('Total Surface Area', cone_tsa(r_cone,l_cone))
with colbco:
    st.metric('Volume',cone_vol(r_cone,l_cone))

##################################################cube#########################
st.divider()
st.subheader('Cube')

col1cu,col2cu = st.columns([1,3])

with col1cu:
   s_cube = st.number_input('side: ',key = "s_cube")

cola_cu,colb_cu = st.columns(2)

with cola_cu:
    st.metric('Total Surface Area',cube_tsa(s_cube))

with colb_cu:
    st.metric('Volume',cube_vol(s_cube))



#########################################cuboid#######################################

st.divider()
st.subheader('Cuboid')

col1r_cu,col2r_cu = st.columns([1,3])

with col1r_cu:
   l = st.number_input('length: ',key = 'cub_l')
   b = st.number_input('breadth: ',key='cub_b')
   h = st.number_input('height: ',key='cub_h')

colar_cu,colbr_cu = st.columns(2)

with colar_cu:
    st.metric('Total Surface Area',cuboid_tsa(l,b,h))

with colbr_cu:
    st.metric('Volume',cuboid_vol(l,b,h))


##################################sphere########################################

st.divider()
st.subheader('Sphere')

col1_sp,col2_sp = st.columns([1,3])

with col1_sp:
   r_sphere = st.number_input('radius: ',key ='r_sphere')

cola_sp,colb_sp = st.columns(2)

with cola_sp:
    st.metric('Total Surface Area',round(sphere_tsa(r_sphere),2))

with colb_sp:
    st.metric('Volume',round(sphere_vol(r_sphere),2))


#####################################cylinder#############################################

st.divider()

st.subheader('Cylinder')

col1cyl,col2cyl = st.columns([1,3])

with col1cyl:
    r_cyl = st.number_input('radius: ',key='r_cyl')
    h_cyl = st.number_input('lateral side length: ',key ='h_cyl')

colacyl,colbcyl = st.columns(2)

with colacyl:
    st.metric('Total Surface Area', cylinder_tsa(r_cyl,h_cyl))
with colbcyl:
    st.metric('Volume',cylinder_vol(r_cyl,h_cyl))
