{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "95eb9de7-545b-4a6e-91e3-2af7ece845a1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "\n",
      "T_ij =  [[ 0.8660254 -0.5        0.         0.       ]\n",
      "         [ 0.5        0.8660254  0.         0.       ]\n",
      "         [ 0.         0.         1.         0.       ]\n",
      "         [ 0.         0.         0.         1.       ]]\n",
      "\n",
      "\n",
      "T_ij =  [[ 0.64278761  0.76604444  0.          5.        ]\n",
      "         [-0.76604444  0.64278761  0.          0.        ]\n",
      "         [ 0.          0.          1.          0.        ]\n",
      "         [ 0.          0.          0.          1.        ]]\n",
      "\n",
      "\n",
      "T_ij =  [[ 0.8660254  0.5        0.         8.       ]\n",
      "         [-0.5        0.8660254  0.         0.       ]\n",
      "         [ 0.         0.         1.         0.       ]\n",
      "         [ 0.         0.         0.         1.       ]]\n",
      "\n",
      "\n",
      "T_ij =  [[ 1. -0.  0.  3.]\n",
      "         [ 0.  1.  0.  0.]\n",
      "         [ 0.  0.  1.  0.]\n",
      "         [ 0.  0.  0.  1.]]\n",
      "Test Case 1:\n",
      "T_01:\n",
      " [[ 0.8660254 -0.5        0.         0.       ]\n",
      " [ 0.5        0.8660254  0.         0.       ]\n",
      " [ 0.         0.         1.         0.       ]\n",
      " [ 0.         0.         0.         1.       ]]\n",
      "T_02:\n",
      " [[ 0.93969262  0.34202014  0.          4.33012702]\n",
      " [-0.34202014  0.93969262  0.          2.5       ]\n",
      " [ 0.          0.          1.          0.        ]\n",
      " [ 0.          0.          0.          1.        ]]\n",
      "T_03:\n",
      " [[ 0.64278761  0.76604444  0.         11.84766799]\n",
      " [-0.76604444  0.64278761  0.         -0.23616115]\n",
      " [ 0.          0.          1.          0.        ]\n",
      " [ 0.          0.          0.          1.        ]]\n",
      "T_04:\n",
      " [[ 0.64278761  0.76604444  0.         13.77603081]\n",
      " [-0.76604444  0.64278761  0.         -2.53429448]\n",
      " [ 0.          0.          1.          0.        ]\n",
      " [ 0.          0.          0.          1.        ]]\n",
      "e1: [13.77603081 -2.53429448  0.        ]\n",
      "\n",
      "\n",
      "T_ij =  [[ 1. -0.  0.  0.]\n",
      "         [ 0.  1.  0.  0.]\n",
      "         [ 0.  0.  1.  0.]\n",
      "         [ 0.  0.  0.  1.]]\n",
      "\n",
      "\n",
      "T_ij =  [[ 1. -0.  0.  5.]\n",
      "         [ 0.  1.  0.  0.]\n",
      "         [ 0.  0.  1.  0.]\n",
      "         [ 0.  0.  0.  1.]]\n",
      "\n",
      "\n",
      "T_ij =  [[ 1. -0.  0.  8.]\n",
      "         [ 0.  1.  0.  0.]\n",
      "         [ 0.  0.  1.  0.]\n",
      "         [ 0.  0.  0.  1.]]\n",
      "\n",
      "\n",
      "T_ij =  [[ 1. -0.  0.  3.]\n",
      "         [ 0.  1.  0.  0.]\n",
      "         [ 0.  0.  1.  0.]\n",
      "         [ 0.  0.  0.  1.]]\n",
      "\n",
      "Test Case 2:\n",
      "T_01:\n",
      " [[ 1. -0.  0.  0.]\n",
      " [ 0.  1.  0.  0.]\n",
      " [ 0.  0.  1.  0.]\n",
      " [ 0.  0.  0.  1.]]\n",
      "T_02:\n",
      " [[1. 0. 0. 5.]\n",
      " [0. 1. 0. 0.]\n",
      " [0. 0. 1. 0.]\n",
      " [0. 0. 0. 1.]]\n",
      "T_03:\n",
      " [[ 1.  0.  0. 13.]\n",
      " [ 0.  1.  0.  0.]\n",
      " [ 0.  0.  1.  0.]\n",
      " [ 0.  0.  0.  1.]]\n",
      "T_04:\n",
      " [[ 1.  0.  0. 16.]\n",
      " [ 0.  1.  0.  0.]\n",
      " [ 0.  0.  1.  0.]\n",
      " [ 0.  0.  0.  1.]]\n",
      "e2: [16.  0.  0.]\n",
      "\n",
      "\n",
      "T_ij =  [[ 0.8660254  0.5        0.         0.       ]\n",
      "         [-0.5        0.8660254  0.         0.       ]\n",
      "         [ 0.         0.         1.         0.       ]\n",
      "         [ 0.         0.         0.         1.       ]]\n",
      "\n",
      "\n",
      "T_ij =  [[ 0.64278761 -0.76604444  0.          5.        ]\n",
      "         [ 0.76604444  0.64278761  0.          0.        ]\n",
      "         [ 0.          0.          1.          0.        ]\n",
      "         [ 0.          0.          0.          1.        ]]\n",
      "\n",
      "\n",
      "T_ij =  [[ 0.8660254 -0.5        0.         8.       ]\n",
      "         [ 0.5        0.8660254  0.         0.       ]\n",
      "         [ 0.         0.         1.         0.       ]\n",
      "         [ 0.         0.         0.         1.       ]]\n",
      "\n",
      "\n",
      "T_ij =  [[ 1. -0.  0.  3.]\n",
      "         [ 0.  1.  0.  0.]\n",
      "         [ 0.  0.  1.  0.]\n",
      "         [ 0.  0.  0.  1.]]\n",
      "\n",
      "Test Case 3:\n",
      "T_01:\n",
      " [[ 0.8660254  0.5        0.         0.       ]\n",
      " [-0.5        0.8660254  0.         0.       ]\n",
      " [ 0.         0.         1.         0.       ]\n",
      " [ 0.         0.         0.         1.       ]]\n",
      "T_02:\n",
      " [[ 0.93969262 -0.34202014  0.          4.33012702]\n",
      " [ 0.34202014  0.93969262  0.         -2.5       ]\n",
      " [ 0.          0.          1.          0.        ]\n",
      " [ 0.          0.          0.          1.        ]]\n",
      "T_03:\n",
      " [[ 0.64278761 -0.76604444  0.         11.84766799]\n",
      " [ 0.76604444  0.64278761  0.          0.23616115]\n",
      " [ 0.          0.          1.          0.        ]\n",
      " [ 0.          0.          0.          1.        ]]\n",
      "T_04:\n",
      " [[ 0.64278761 -0.76604444  0.         13.77603081]\n",
      " [ 0.76604444  0.64278761  0.          2.53429448]\n",
      " [ 0.          0.          1.          0.        ]\n",
      " [ 0.          0.          0.          1.        ]]\n",
      "e3: [13.77603081  2.53429448  0.        ]\n"
     ]
    }
   ],
   "source": [
    "#!/usr/bin/env python\n",
    "# coding: utf-8\n",
    "\n",
    "# ![](https://github.com/eraldoribeiro/assignment_robotarm2D/blob/main/robotArm01.png?raw=1)\n",
    "# *Figure 1*: A two-dimensional articulated arm. The articulated structure has 3 local coordinate frames each one centered at a joint. For each part, the local x-axis is aligned with the part.\n",
    "\n",
    "\"\"\"\n",
    "Spheres and cylinders\n",
    "\"\"\"\n",
    "# (adapted from http://www.glowscript.org)\n",
    "from vedo import *\n",
    "import numpy as np\n",
    "\n",
    "# Color of robot arm\n",
    "robotColor = \"green\"\n",
    "jointColor = \"white\"\n",
    "\n",
    "\n",
    "def RotationMatrix(theta, axis_name):\n",
    "    \"\"\" calculate single rotation of \\(\\theta\\) matrix around x,y or z\n",
    "        code from: https://programming-surgeon.com/en/euler-angle-python-en/\n",
    "    input\n",
    "        theta = rotation angle(degrees)\n",
    "        axis_name = 'x', 'y' or 'z'\n",
    "    output\n",
    "        3x3 rotation matrix\n",
    "    \"\"\"\n",
    "\n",
    "    c = np.cos(theta * np.pi / 180)\n",
    "    s = np.sin(theta * np.pi / 180)\n",
    "    if axis_name == 'x':\n",
    "        rotation_matrix = np.array([[1, 0,  0],\n",
    "                                    [0, c, -s],\n",
    "                                    [0, s,  c]])\n",
    "    if axis_name == 'y':\n",
    "        rotation_matrix = np.array([[c,  0, s],\n",
    "                                    [0,  1, 0],\n",
    "                                    [-s,  0, c]])\n",
    "    elif axis_name == 'z':\n",
    "        rotation_matrix = np.array([[c, -s, 0],\n",
    "                                    [s,  c, 0],\n",
    "                                    [0,  0, 1]])\n",
    "    return rotation_matrix\n",
    "\n",
    "\n",
    "def createCoordinateFrameMesh():\n",
    "    \"\"\"Returns the mesh representing a coordinate frame\n",
    "    Args:\n",
    "      No input args\n",
    "    Returns:\n",
    "      F: vedo.mesh object (arrows for axis)\n",
    "\n",
    "    \"\"\"     \n",
    "\n",
    "    _shaft_radius = 0.05\n",
    "    _head_radius = 0.10\n",
    "    _alpha = 1\n",
    "\n",
    "    # x-axis as an arrow  \n",
    "    x_axisArrow = Arrow(\n",
    "                    start_pt=(0, 0, 0),\n",
    "                    end_pt=(1, 0, 0),\n",
    "                    s=None,\n",
    "                    shaft_radius=_shaft_radius,\n",
    "                    head_radius=_head_radius,\n",
    "                    head_length=None,\n",
    "                    res=12,\n",
    "                    c='red',\n",
    "                    alpha=_alpha\n",
    "    )\n",
    "\n",
    "    # y-axis as an arrow  \n",
    "    y_axisArrow = Arrow(\n",
    "                    start_pt=(0, 0, 0),\n",
    "                    end_pt=(0, 1, 0),\n",
    "                    s=None,\n",
    "                    shaft_radius=_shaft_radius,\n",
    "                    head_radius=_head_radius,\n",
    "                    head_length=None,\n",
    "                    res=12,\n",
    "                    c='green',\n",
    "                    alpha=_alpha\n",
    "    )\n",
    "\n",
    "    # z-axis as an arrow  \n",
    "    z_axisArrow = Arrow(\n",
    "                    start_pt=(0, 0, 0),\n",
    "                    end_pt=(0, 0, 1),\n",
    "                    s=None,\n",
    "                    shaft_radius=_shaft_radius,\n",
    "                    head_radius=_head_radius,\n",
    "                    head_length=None,\n",
    "                    res=12,\n",
    "                    c='blue',\n",
    "                    alpha=_alpha\n",
    "    )\n",
    "\n",
    "    originDot = Sphere(pos=[0,0,0], \n",
    "                       c=\"black\", \n",
    "                       r=0.10)\n",
    "\n",
    "    # Combine the axes together to form a frame\n",
    "    F = x_axisArrow + y_axisArrow + z_axisArrow + originDot\n",
    "\n",
    "    return F\n",
    "\n",
    "\n",
    "def getLocalFrameMatrix(R_ij, t_ij): \n",
    "    \"\"\"Returns the matrix representing the local frame\n",
    "    Args:\n",
    "      R_ij: rotation of Frame j w.r.t. Frame i \n",
    "      t_ij: translation of Frame j w.r.t. Frame i \n",
    "    Returns:\n",
    "      T_ij: Matrix of Frame j w.r.t. Frame i. \n",
    "\n",
    "    \"\"\"             \n",
    "    # Rigid-body transformation [ R t ]\n",
    "    T_ij = np.block([[R_ij,                t_ij],\n",
    "                     [np.zeros((1, 3)),       1]])\n",
    "    print('\\n')\n",
    "    print('T_ij = ', np.array2string(T_ij, prefix='        '))\n",
    "\n",
    "    return T_ij\n",
    "\n",
    "\n",
    "def forward_kinematics1(Phi, L1, L2, L3, L4):\n",
    "    \"\"\"Calculate the local-to-global frame matrices, \n",
    "    and the location of the end-effector.\n",
    "    \n",
    "    Args:\n",
    "        Phi (4x1 nd.array): Array containing the four joint angles  \n",
    "        L1, L2, L3, L4 (float): lengths of the parts\n",
    "        \n",
    "    Returns: \n",
    "        T_01, T_02, T_03, T_04: 4x4 nd.arrays, local-to-global matrices \n",
    "        e: 3x1 nd.array, location of end-effector \n",
    "    \"\"\"\n",
    "    \n",
    "    R_01 = RotationMatrix(Phi[0], 'z')  \n",
    "    R_12 = RotationMatrix(Phi[1], 'z')\n",
    "    R_23 = RotationMatrix(Phi[2], 'z')\n",
    "    R_34 = RotationMatrix(Phi[3], 'z')\n",
    "\n",
    "    t_01 = np.array([[0], [0], [0]])\n",
    "    t_12 = np.array([[L1], [0], [0]])\n",
    "    t_23 = np.array([[L2], [0], [0]]) \n",
    "    t_34 = np.array([[L3], [0], [0]])\n",
    "\n",
    "    T_01 = getLocalFrameMatrix(R_01, t_01) \n",
    "    T_12 = getLocalFrameMatrix(R_12, t_12)\n",
    "    T_23 = getLocalFrameMatrix(R_23, t_23)\n",
    "    T_34 = getLocalFrameMatrix(R_34, t_34)\n",
    "\n",
    "    T_02 = T_01 @ T_12 \n",
    "    T_03 = T_02 @ T_23\n",
    "    T_04 = T_03 @ T_34\n",
    "\n",
    "    e = T_04[:3, 3]\n",
    "    \n",
    "    return T_01, T_02, T_03, T_04, e\n",
    "\n",
    "\n",
    "def forward_kinematics2(Phi, L1, L2, L3, L4):\n",
    "    R_01 = RotationMatrix(Phi[0], 'z')  \n",
    "    R_12 = RotationMatrix(Phi[1], 'z')\n",
    "    R_23 = RotationMatrix(Phi[2], 'z')\n",
    "    R_34 = RotationMatrix(Phi[3], 'z')\n",
    "\n",
    "    t_01 = np.array([[0], [0], [0]])\n",
    "    t_12 = np.array([[L1], [0], [0]])\n",
    "    t_23 = np.array([[L2], [0], [0]]) \n",
    "    t_34 = np.array([[L3], [0], [0]])\n",
    "\n",
    "    T_01 = getLocalFrameMatrix(R_01, t_01) \n",
    "    T_12 = getLocalFrameMatrix(R_12, t_12)\n",
    "    T_23 = getLocalFrameMatrix(R_23, t_23)\n",
    "    T_34 = getLocalFrameMatrix(R_34, t_34)\n",
    "\n",
    "    T_02 = T_01 @ T_12 \n",
    "    T_03 = T_02 @ T_23\n",
    "    T_04 = T_03 @ T_34\n",
    "\n",
    "    e = T_04[:3, 3]\n",
    "    \n",
    "    return T_01, T_02, T_03, T_04, e\n",
    "\n",
    "\n",
    "def forward_kinematics3(Phi, L1, L2, L3, L4):\n",
    "    R_01 = RotationMatrix(Phi[0], 'z')  \n",
    "    R_12 = RotationMatrix(Phi[1], 'z')\n",
    "    R_23 = RotationMatrix(Phi[2], 'z')\n",
    "    R_34 = RotationMatrix(Phi[3], 'z')\n",
    "\n",
    "    t_01 = np.array([[0], [0], [0]])\n",
    "    t_12 = np.array([[L1], [0], [0]])\n",
    "    t_23 = np.array([[L2], [0], [0]]) \n",
    "    t_34 = np.array([[L3], [0], [0]])\n",
    "\n",
    "    T_01 = getLocalFrameMatrix(R_01, t_01) \n",
    "    T_12 = getLocalFrameMatrix(R_12, t_12)\n",
    "    T_23 = getLocalFrameMatrix(R_23, t_23)\n",
    "    T_34 = getLocalFrameMatrix(R_34, t_34)\n",
    "\n",
    "    T_02 = T_01 @ T_12 \n",
    "    T_03 = T_02 @ T_23\n",
    "    T_04 = T_03 @ T_34\n",
    "\n",
    "    e = T_04[:3, 3]\n",
    "    \n",
    "    return T_01, T_02, T_03, T_04, e\n",
    "\n",
    "\n",
    "# Example of usage in the test cases:\n",
    "L1, L2, L3, L4 = [5, 8, 3, 0]\n",
    "\n",
    "# Test Case 1\n",
    "Phi1 = np.array([30, -50, -30, 0])\n",
    "T_01, T_02, T_03, T_04, e1 = forward_kinematics1(Phi1, L1, L2, L3, L4)\n",
    "print(\"Test Case 1:\")\n",
    "print(\"T_01:\\n\", T_01)\n",
    "print(\"T_02:\\n\", T_02)\n",
    "print(\"T_03:\\n\", T_03)\n",
    "print(\"T_04:\\n\", T_04)\n",
    "print(\"e1:\", e1)\n",
    "\n",
    "# Test Case 2\n",
    "Phi2 = np.array([0, 0, 0, 0])\n",
    "T_01, T_02, T_03, T_04, e2 = forward_kinematics2(Phi2, L1, L2, L3, L4)\n",
    "print(\"\\nTest Case 2:\")\n",
    "print(\"T_01:\\n\", T_01)\n",
    "print(\"T_02:\\n\", T_02)\n",
    "print(\"T_03:\\n\", T_03)\n",
    "print(\"T_04:\\n\", T_04)\n",
    "print(\"e2:\", e2)\n",
    "\n",
    "# Test Case 3\n",
    "Phi3 = np.array([-30, 50, 30, 0])\n",
    "T_01, T_02, T_03, T_04, e3 = forward_kinematics3(Phi3, L1, L2, L3, L4)\n",
    "print(\"\\nTest Case 3:\")\n",
    "print(\"T_01:\\n\", T_01)\n",
    "print(\"T_02:\\n\", T_02)\n",
    "print(\"T_03:\\n\", T_03)\n",
    "print(\"T_04:\\n\", T_04)\n",
    "print(\"e3:\", e3)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "83f547b0-5142-41ac-8feb-31d02cf89310",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
