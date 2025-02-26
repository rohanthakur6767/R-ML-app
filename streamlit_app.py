import streamlit as st
import trimesh
import plotly.graph_objects as go

# Set Streamlit app title
st.title("🧸 3D Teddy Bear Viewer")

# Upload 3D model file
uploaded_file = st.file_uploader("Upload a 3D model (STL or OBJ)", type=["stl", "obj"])

if uploaded_file is not None:
    try:
        # Load the 3D model
        mesh = trimesh.load_mesh(uploaded_file)

        # Convert the model to Plotly format
        fig = go.Figure(data=[go.Mesh3d(
            x=mesh.vertices[:, 0],
            y=mesh.vertices[:, 1],
            z=mesh.vertices[:, 2],
            i=mesh.faces[:, 0],
            j=mesh.faces[:, 1],
            k=mesh.faces[:, 2],
            color='brown',
            opacity=0.9
        )])

        # Display the 3D model
        st.plotly_chart(fig)

    except Exception as e:
        st.error(f"Error loading 3D model: {e}")
else:
    st.info("Upload a 3D model file to view it here.")
