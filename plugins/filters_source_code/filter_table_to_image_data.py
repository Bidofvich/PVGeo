Name = 'Table To ImageData'
Label = 'Table To ImageData'
Help = 'This filter takes a vtkTable object with columns that represent data to be translated (reshaped) into a 3D grid (2D also works, just set the third dimensions extent to 1). The grid will be a nx by ny by nz structure and an origin can be set at any xyz point.'

NumberOfInputs = 1
InputDataType = 'vtkTable'
OutputDataType = 'vtkImageData'
ExtraXml = '''\
<Hints>
    <ShowInMenu category="CSM GP Filters" />
</Hints>
'''

Properties = dict(
    nx=1,
    ny=1,
    nz=1,
    x_spacing=1,
    y_spacing=1,
    z_spacing=1,
    x_origin=0,
    y_origin=0,
    z_origin=0,
)

def RequestData():
    pdi = self.GetInput()
    image = self.GetOutput() #vtkImageData
    cols = pdi.GetNumberOfColumns()

    # Setup the ImageData
    image.SetDimensions(nx, ny, nz)
    image.SetOrigin(x_origin, y_origin, z_origin)
    image.SetSpacing(x_spacing, y_spacing, z_spacing)
    image.SetExtent(0,nx-1, 0,ny-1, 0,nz-1)

    # Add all columns of the table as arrays to the PointData
    for i in range(cols):
        c = pdi.GetColumn(i)
        #image.GetCellData().AddArray(c) # Should we add here? flipper won't flip these...
        image.GetPointData().AddArray(c)


def RequestInformation():
    from paraview import util
    # ABSOLUTELY NECESSARY FOR THE FILTER TO WORK:
    util.SetOutputWholeExtent(self, [0,nx-1, 0,ny-1, 0,nz-1])
