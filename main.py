import vtk

def main():
    cubeSource = vtk.vtkCubeSource()
    cubeMapper = vtk.vtkPolyDataMapper()
    cubeMapper.SetInputConnection(cubeSource.GetOutputPort())
    
    cubeActor = vtk.vtkActor()
    cubeActor.GetProperty().SetOpacity(0.5)
    cubeActor.SetMapper(cubeMapper)
    
    sphereSource = vtk.vtkSphereSource()
    sphereMapper = vtk.vtkPolyDataMapper()
    sphereMapper.SetInputConnection(sphereSource.GetOutputPort());
    
    sphereActor = vtk.vtkActor()
    sphereActor.GetProperty().SetColor(0.5,1,0.5);
    #sphereActor.GetProperty().SetOpacity(0.5);
    sphereActor.SetMapper(sphereMapper);
    
    renderer = vtk.vtkRenderer()
    renderer.AddActor(cubeActor);
    renderer.AddActor(sphereActor);
    
    renderWindow = vtk.vtkRenderWindow()
    renderWindow.AddRenderer(renderer);
    
    interactor = vtk.vtkRenderWindowInteractor()
    interactor.SetRenderWindow(renderWindow);
    renderer.SetBackground(0,0,0);
    renderWindow.Render();
    
    interactor.Start();

if __name__ == '__main__':
    main()