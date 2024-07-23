import { Child } from "./child.interface";

export interface Team {
  id: number;
  name: string;
  children: Child[];
}
