{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "95eb9de7-545b-4a6e-91e3-2af7ece845a1",
   "metadata": {},
   "outputs": [
    {
     "ename": "RecursionError",
     "evalue": "maximum recursion depth exceeded",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mRecursionError\u001b[0m                            Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[8], line 229\u001b[0m\n\u001b[0;32m    227\u001b[0m \u001b[38;5;66;03m# Test Case 1\u001b[39;00m\n\u001b[0;32m    228\u001b[0m Phi \u001b[38;5;241m=\u001b[39m np\u001b[38;5;241m.\u001b[39marray([\u001b[38;5;241m30\u001b[39m, \u001b[38;5;241m-\u001b[39m\u001b[38;5;241m50\u001b[39m, \u001b[38;5;241m-\u001b[39m\u001b[38;5;241m30\u001b[39m, \u001b[38;5;241m0\u001b[39m])\n\u001b[1;32m--> 229\u001b[0m T_01, T_02, T_03, T_04, e \u001b[38;5;241m=\u001b[39m \u001b[43mforward_kinematics1\u001b[49m\u001b[43m(\u001b[49m\u001b[43mPhi\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mL1\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mL2\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mL3\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mL4\u001b[49m\u001b[43m)\u001b[49m\n\u001b[0;32m    230\u001b[0m \u001b[38;5;28mprint\u001b[39m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mTest Case 1:\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n\u001b[0;32m    231\u001b[0m \u001b[38;5;28mprint\u001b[39m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mT_01:\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m, T_01)\n",
      "Cell \u001b[1;32mIn[8], line 143\u001b[0m, in \u001b[0;36mforward_kinematics1\u001b[1;34m(Phi, L1, L2, L3, L4)\u001b[0m\n\u001b[0;32m    141\u001b[0m \u001b[38;5;66;03m# Test Case 1\u001b[39;00m\n\u001b[0;32m    142\u001b[0m Phi \u001b[38;5;241m=\u001b[39m np\u001b[38;5;241m.\u001b[39marray([\u001b[38;5;241m30\u001b[39m, \u001b[38;5;241m-\u001b[39m\u001b[38;5;241m50\u001b[39m, \u001b[38;5;241m-\u001b[39m\u001b[38;5;241m30\u001b[39m, \u001b[38;5;241m0\u001b[39m])\n\u001b[1;32m--> 143\u001b[0m T_01, T_02, T_03, T_04, e \u001b[38;5;241m=\u001b[39m \u001b[43mforward_kinematics1\u001b[49m\u001b[43m(\u001b[49m\u001b[43mPhi\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mL1\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mL2\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mL3\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mL4\u001b[49m\u001b[43m)\u001b[49m\n\u001b[0;32m    144\u001b[0m R_01 \u001b[38;5;241m=\u001b[39m RotationMatrix(Phi[\u001b[38;5;241m0\u001b[39m], \u001b[38;5;124m'\u001b[39m\u001b[38;5;124mz\u001b[39m\u001b[38;5;124m'\u001b[39m)  \n\u001b[0;32m    145\u001b[0m R_12 \u001b[38;5;241m=\u001b[39m RotationMatrix(Phi[\u001b[38;5;241m1\u001b[39m], \u001b[38;5;124m'\u001b[39m\u001b[38;5;124mz\u001b[39m\u001b[38;5;124m'\u001b[39m)\n",
      "Cell \u001b[1;32mIn[8], line 143\u001b[0m, in \u001b[0;36mforward_kinematics1\u001b[1;34m(Phi, L1, L2, L3, L4)\u001b[0m\n\u001b[0;32m    141\u001b[0m \u001b[38;5;66;03m# Test Case 1\u001b[39;00m\n\u001b[0;32m    142\u001b[0m Phi \u001b[38;5;241m=\u001b[39m np\u001b[38;5;241m.\u001b[39marray([\u001b[38;5;241m30\u001b[39m, \u001b[38;5;241m-\u001b[39m\u001b[38;5;241m50\u001b[39m, \u001b[38;5;241m-\u001b[39m\u001b[38;5;241m30\u001b[39m, \u001b[38;5;241m0\u001b[39m])\n\u001b[1;32m--> 143\u001b[0m T_01, T_02, T_03, T_04, e \u001b[38;5;241m=\u001b[39m \u001b[43mforward_kinematics1\u001b[49m\u001b[43m(\u001b[49m\u001b[43mPhi\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mL1\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mL2\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mL3\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mL4\u001b[49m\u001b[43m)\u001b[49m\n\u001b[0;32m    144\u001b[0m R_01 \u001b[38;5;241m=\u001b[39m RotationMatrix(Phi[\u001b[38;5;241m0\u001b[39m], \u001b[38;5;124m'\u001b[39m\u001b[38;5;124mz\u001b[39m\u001b[38;5;124m'\u001b[39m)  \n\u001b[0;32m    145\u001b[0m R_12 \u001b[38;5;241m=\u001b[39m RotationMatrix(Phi[\u001b[38;5;241m1\u001b[39m], \u001b[38;5;124m'\u001b[39m\u001b[38;5;124mz\u001b[39m\u001b[38;5;124m'\u001b[39m)\n",
      "    \u001b[1;31m[... skipping similar frames: forward_kinematics1 at line 143 (2971 times)]\u001b[0m\n",
      "Cell \u001b[1;32mIn[8], line 143\u001b[0m, in \u001b[0;36mforward_kinematics1\u001b[1;34m(Phi, L1, L2, L3, L4)\u001b[0m\n\u001b[0;32m    141\u001b[0m \u001b[38;5;66;03m# Test Case 1\u001b[39;00m\n\u001b[0;32m    142\u001b[0m Phi \u001b[38;5;241m=\u001b[39m np\u001b[38;5;241m.\u001b[39marray([\u001b[38;5;241m30\u001b[39m, \u001b[38;5;241m-\u001b[39m\u001b[38;5;241m50\u001b[39m, \u001b[38;5;241m-\u001b[39m\u001b[38;5;241m30\u001b[39m, \u001b[38;5;241m0\u001b[39m])\n\u001b[1;32m--> 143\u001b[0m T_01, T_02, T_03, T_04, e \u001b[38;5;241m=\u001b[39m \u001b[43mforward_kinematics1\u001b[49m\u001b[43m(\u001b[49m\u001b[43mPhi\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mL1\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mL2\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mL3\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mL4\u001b[49m\u001b[43m)\u001b[49m\n\u001b[0;32m    144\u001b[0m R_01 \u001b[38;5;241m=\u001b[39m RotationMatrix(Phi[\u001b[38;5;241m0\u001b[39m], \u001b[38;5;124m'\u001b[39m\u001b[38;5;124mz\u001b[39m\u001b[38;5;124m'\u001b[39m)  \n\u001b[0;32m    145\u001b[0m R_12 \u001b[38;5;241m=\u001b[39m RotationMatrix(Phi[\u001b[38;5;241m1\u001b[39m], \u001b[38;5;124m'\u001b[39m\u001b[38;5;124mz\u001b[39m\u001b[38;5;124m'\u001b[39m)\n",
      "\u001b[1;31mRecursionError\u001b[0m: maximum recursion depth exceeded"
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
    "    # Example of usage in the test cases:\n",
    "    L1, L2, L3, L4 = [5, 8, 3, 0]\n",
    "\n",
    "    # Test Case 1\n",
    "    Phi = np.array([30, -50, -30, 0])\n",
    "    T_01, T_02, T_03, T_04, e = forward_kinematics1(Phi, L1, L2, L3, L4)\n",
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
    "    L1, L2, L3, L4 = [5, 8, 3, 0]\n",
    "    Phi = np.array([0, 0, 0, 0])\n",
    "    T_01, T_02, T_03, T_04, e = forward_kinematics2(Phi, L1, L2, L3, L4)\n",
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
    "    L1, L2, L3, L4 = [5, 8, 3, 0]\n",
    "    Phi = np.array([-30, 50, 30, 0])\n",
    "    T_01, T_02, T_03, T_04, e = forward_kinematics3(Phi, L1, L2, L3, L4)\n",
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
    "Phi = np.array([30, -50, -30, 0])\n",
    "T_01, T_02, T_03, T_04, e = forward_kinematics1(Phi, L1, L2, L3, L4)\n",
    "print(\"Test Case 1:\")\n",
    "print(\"T_01:\\n\", T_01)\n",
    "print(\"T_02:\\n\", T_02)\n",
    "print(\"T_03:\\n\", T_03)\n",
    "print(\"T_04:\\n\", T_04)\n",
    "print(\"e1:\", e)\n",
    "\n",
    "# Test Case 2\n",
    "Phi = np.array([0, 0, 0, 0])\n",
    "T_01, T_02, T_03, T_04, e2 = forward_kinematics2(Phi, L1, L2, L3, L4)\n",
    "print(\"\\nTest Case 2:\")\n",
    "print(\"T_01:\\n\", T_01)\n",
    "print(\"T_02:\\n\", T_02)\n",
    "print(\"T_03:\\n\", T_03)\n",
    "print(\"T_04:\\n\", T_04)\n",
    "print(\"e2:\", e)\n",
    "\n",
    "# Test Case 3\n",
    "Phi = np.array([-30, 50, 30, 0])\n",
    "T_01, T_02, T_03, T_04, e = forward_kinematics3(Phi, L1, L2, L3, L4)\n",
    "print(\"\\nTest Case 3:\")\n",
    "print(\"T_01:\\n\", T_01)\n",
    "print(\"T_02:\\n\", T_02)\n",
    "print(\"T_03:\\n\", T_03)\n",
    "print(\"T_04:\\n\", T_04)\n",
    "print(\"e3:\", e)\n"
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
